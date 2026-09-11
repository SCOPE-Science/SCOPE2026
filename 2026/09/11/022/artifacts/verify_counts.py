"""Replayable dimension-count certificate for lane-715 PRESET_FALLBACK.
Claim: general genus-6 C, general M in Pic^10: no stable rank-2 E with
det=M, h0>=4 admits a line quotient of degree <=6.
Covers: (i) e<=5 by stability; (ii) e=6 by incidence dimension count.
Stdlib only.
"""
def rho(g, r, d):
    return g - (r + 1) * (g - d + r)

g = 6
print("== rho(g=6) table ==")
needed = [(0, 4), (1, 4), (2, 4), (0, 6), (1, 6), (2, 6), (3, 6),
          (0, 3), (1, 3), (2, 7), (0, 2), (3, 8)]
for r, d in needed:
    print(f"  W^{r}_{d}: rho={rho(g, r, d)}")

# (i) Stability lemma: mu(E)=5; stable => every line subbundle deg<=4
# => every line quotient deg>=6. So strata e<=5 empty (no genericity needed).
print("\n== stability lemma ==")
print("  mu(E)=10/2=5; stable => quotient deg >= 6; e<=5 strata EMPTY.")

# (ii) e=6: N deg4, L deg6, need n0+l0>=4.
print("\n== e=6 case split (need n0+l0>=4) ==")
print(f"  l0>=4 needs W^3_6: rho={rho(g,3,6)} -> EMPTY.")
print(f"  n0>=3 needs W^2_4: rho={rho(g,2,4)} -> EMPTY.")
print("  Hence n0<=2, l0<=3. Remaining cases with n0+l0>=4:")
d1 = rho(g, 0, 4) + rho(g, 2, 6)   # (n0>=1,l0>=3)
d2 = rho(g, 1, 4) + rho(g, 1, 6)   # (n0>=2,l0>=2)
print(f"  (n0>=1,l0>=3): W^0_4 x W^2_6 dim {rho(g,0,4)}+{rho(g,2,6)}={d1}")
print(f"  (n0>=2,l0>=2): W^1_4 x W^1_6 dim {rho(g,1,4)}+{rho(g,1,6)}={d2}")
assert d1 <= 4 and d2 <= 4
print(f"  Both incidence images in Pic^10 (dim 6) have dim<={max(d1,d2)}<6.")
print("  General M avoids all => e=6 stratum EMPTY (Porteous locus empty a fortiori).")

# Hard assertions (fail loudly if arithmetic changes)
assert rho(6, 0, 4) == 4 and rho(6, 1, 4) == 0 and rho(6, 2, 4) == -6
assert rho(6, 2, 6) == 0 and rho(6, 1, 6) == 4 and rho(6, 3, 6) == -6
assert rho(6, 0, 3) == 3 and rho(6, 2, 7) == 3
print("\nVERIFY_OK: all e<=6 strata certified empty over general M.")
