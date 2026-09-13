# Correct model: B-traces (0,1,c),(0,2,c): w-lines. List them and match to w=(m/2)z prediction.
# Traces above (u,v,w)=(x1,w,z): B-traces: (0,1,-2),(0,1,-1),(0,1,0),(0,1,1),(0,2,-1),(0,2,1).
# (0,1,c): w + c z = 0 → w = -c z, c in {-2,-1,0,1} → w in {2,1,0,-1}z. (0,2,c): 2w+c z=0 → w=-c/2 z = ±1/2 z.
# So W = {-1,0,1,2} (from x2,x3 traces) ∪ {±1/2} (from x2+x3 traces with odd m) = 6 lines?!
# But count shows only 6 B-traces: 4 of type (0,1,*)+2 of type (0,2,*) = 6. ✓.
# So |W|=6 for k=2, and total |R| = 4(A)+6(B)+4(C)+4(D)+1(inf) = 19 ✓ matches!
# My verify_counts.py "S" was WRONG: it used S = M ∪ {m/2 : m ∈ M} = {-1,-1/2,0,1/2,1,2} (6 elements) — actually correct!
# len(S) for k=2 is 6, not 4. But stats printed B=18=N? N should be 4+6+4+4+1 = 19, but stats B (=N) printed... count_ck2 printed only P2..Delta, not N. verify_counts printed N=18?! Contradiction — recheck.
# verify_counts built lines as A(M)+B(S)+C(M)+D(M) WITHOUT infinity line: 4+6+4+4=18. The arrangement R includes z=0 trace (inf line) → 19. chi of central R = (t-1)*chi(deconed). Fine.
# And Ssize formula in analytic_check was wrong (2k+(k%2)); true |S| = 2k + #{odd m in M} = 2k+k = 3k.
# Redo exact counts: |S|=3k (M has k odds? M={-k+1..k}: count odds = k. k=1:{0,1}→{1}:1 ✓; k=2:{-1,0,1,2}→{-1,1}:2 ✓; k=3:{-2..3}→{-1,1,3}:3 ✓. yes k odds.)
# So |S| = |M| + k = 3k (halves of odd m are new; halves of even m lie in M... need: m/2 for even m: m=2j → j; is j always in M? j in [-k/2+..]. m ∈ M even → m/2 ∈ [-(k-1)/2, k/2]; M=[-k+1,k] contains it ✓. odd m → m/2 half-integer ∉ M ✓ new. distinct ✓.)
# P2 = AB+AC+AD+BC+BD+CD = (2k)(3k)+4k²+4k²+(3k)(2k)+(3k)(2k)+4k² = 6k²+4k²+4k²+6k²+6k²+4k² = 30k².
# k=1: 30 ✓; k=2: 120 ✓; k=3: 270 ✓. 
# ABC: a∈M,b∈S, a-b∈M. b∈M: 3k² (computed). b∈S\M (odd halves): a-b ∈ M? a integer... a - (odd/2) = half-integer ∉ M (M integers) → 0. So ABC=3k² ✓ (matches 3,12,27,48).
# ABD same = 3k² ✓. ACD = 2k² (verify below). Q: b odd-half → a±b half-integer ∉ M → Q from MxM only = 2k² (verify below).
# BCD = #{(c,d)∈M² : (d-c)/2 ∈ S}: verify formula below.
from fractions import Fraction
def Sset(k):
    M = list(range(-k+1, k+1))
    S = sorted(set([Fraction(a) for a in M]) | set([Fraction(a,2) for a in M]))
    return M, S
for k in range(1,7):
    M, S = Sset(k)
    print(f"k={k}: |M|={len(M)} |S|={len(S)} S={[str(x) for x in S]}")
# ACD closed form: sum_{a∈M} #{(c,d)∈M²: c+d=2a}. M={-k+1..k}, |M|=2k. #pairs with sum s: for s in [2(-k+1), 2k]: N(s) = 2k-|s-1/2|... compute: values give 2k² total. proof: pairs (c,d): c+d=2a ↔ (c-a)+(d-a)=0, u+v=0 with u,v ∈ M-a. M-a = {-k+1-a, ..., k-a} ∋ 0 (since a∈M). #{u : u,-u ∈ M-a} = #{u: both in interval} = 2*min(a-(-k+1), k-a)+1 = 2*min(a+k-1,k-a)+1. sum over a: substitute j=a+k-1 ∈ {0,...,2k-1}: min(j, 2k-1-j)... = 2*sum... = 2k²? check: k=2: a∈{-1,0,1,2}: counts 2*min(a+1,2-a)+1: a=-1:1, a=0:3, a=1:3, a=2:1 → 8=2k² ✓.
print("ACD formula check done in analysis.")
# Q closed form: #{(a,b)∈M²: a-b,a+b∈M} = 2k²? k=2: 8 ✓ brute. proof: u=a-b,v=a+b ∈ M, u,v same parity (u+v=2a even). # = #{(u,v)∈M²: u+v even} (a=(u+v)/2 ∈ M? (u+v)/2 ∈ [-k+1,k]? u+v ∈ [-2k+2,2k], half ∈ [-k+1,k] ✓ always). #{(u,v)∈M² same parity} = (#even)²+(#odd)² = k²+k² = 2k² ✓ (M has k evens, k odds: M={-k+1..k} consecutive 2k numbers → k,k ✓).
print("Q formula: (#even)^2+(#odd)^2 = 2k^2 ✓")
# BCD: #{(c,d)∈M² : (d-c)/2 ∈ S}, S = M ∪ {odd halves... as Fractions: S = {integers in M} ∪ {m/2: m odd in M}}.
# (d-c)/2 ∈ S ⟺ (d-c)/2 ∈ M i.e. d-c ∈ 2M (even integers in [-2k+2,2k]) OR (d-c)/2 = m/2 for odd m ∈ M i.e. d-c ∈ M_odd = {odd m ∈ M}.
# So condition: d-c ∈ 2M ∪ M_odd. 2M = even ints in [-2k+2, 2k]; M_odd = odd ints in [-k+1,k].
# count = sum_e N_e 1[e ∈ 2M ∪ M_odd], N_e = 2k-|e|, e ∈ [-(2k-1), 2k-1].
for k in range(1,7):
    M = list(range(-k+1, k+1))
    twoM = set(2*m for m in M)
    Modd = set(m for m in M if m % 2 != 0)
    cond = twoM | Modd
    tot = sum((2*k - abs(e)) for e in range(-(2*k-1), 2*k) if e in cond)
    # brute
    Sh = set(Fraction(a) for a in M) | set(Fraction(a,2) for a in M)
    brute = sum(1 for c in M for d in M if (Fraction(d-c,2)) in Sh)
    print(f"k={k}: formula={tot} brute={brute} {'OK' if tot==brute else 'MISMATCH'}")
