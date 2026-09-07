"""Detect minimal candidate (N0, p) by longest-suffix match with p <= 1000.

For each p in 1..1000: find largest N0 such that G[n] == G[n+p] for all
n in [N0, Nmax-p]. Report candidates with smallest N0 / longest stable window.
Also verify the specific claim (N0=259, p=148).
"""
import csv
import sys

csv_path = sys.argv[1] if len(sys.argv) > 1 else "output/artifacts/grundy_0057_N8000.csv"
G = {}
with open(csv_path) as f:
    r = csv.DictReader(f)
    for row in r:
        G[int(row["heap"])] = int(row["grundy"])
Nmax = max(G)
print("Nmax =", Nmax)

# check specific claim first
N0c, pc = 259, 148
bad = [n for n in range(N0c, Nmax - pc + 1) if G[n] != G[n + pc]]
print("claim (259,148): mismatches =", len(bad), "first few:", bad[:10])

# full scan p <= 1000: compute minimal N0(p) = first index from which suffix matches
results = []
for p in range(1, 1001):
    n = Nmax - p
    while n >= 0 and G[n] == G[n + p]:
        n -= 1
    N0 = n + 1  # suffix [N0, Nmax-p] matches
    results.append((N0, p, Nmax - p - N0 + 1))

# sort by N0 then p
results.sort()
print("top 15 by smallest N0:")
for N0, p, wlen in results[:15]:
    print("  N0=%d p=%d window_len=%d" % (N0, p, wlen))

# among small N0, longest window
print("candidates with N0<=400 and window>=3000:")
for N0, p, wlen in sorted(results, key=lambda t: -t[2]):
    if N0 <= 400 and wlen >= 3000:
        print("  N0=%d p=%d window_len=%d" % (N0, p, wlen))
    if wlen < 3000:
        break
