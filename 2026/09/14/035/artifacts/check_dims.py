"""Numerical checks for lane-1928 target: dims, genera, fiber dims."""
# Genus g=2, rank r=3.
g = 2
r = 3
# h0(K^i) via Riemann-Roch for deg > 2g-2, else g.
# deg K^i = i*(2g-2) = 2i.
# i=1: deg 2 = 2g-2, h0 = g = 2 (special).
h0_K = g
# i=2: deg 4 > 2, h0 = deg - g + 1 = 4-2+1 = 3.
h0_K2 = 4 - g + 1
# i=3: deg 6, h0 = 6-2+1 = 5.
h0_K3 = 6 - g + 1
dimB = h0_K + h0_K2 + h0_K3
# dim M(GL_r Higgs, stable) = 2 + 2 r^2 (g-1)
dimM = 2 + 2*r*r*(g-1)
# spectral arithmetic genus via Riemann-Hurwitz for deg-r cover:
# branch degree = deg K^{r(r-1)} = r(r-1)(2g-2)/... deg K^m = m*2.
# For r=3: disc in K^6, deg 12.
deg_disc = 6*2
# 2 g_S - 2 = r*(2g-2) + deg_disc
gS = (r*(2*g-2) + deg_disc + 2)//2
# nodal: geometric genus = gS - 1
g_geom_nodal = gS - 1
# generalized Jacobian dim = gS; abelian part dim = g_geom
print(f"h0(K)={h0_K}, h0(K^2)={h0_K2}, h0(K^3)={h0_K3}, dimB={dimB}")
print(f"dimM={dimM}, rel dim={dimM-dimB}")
print(f"deg disc={deg_disc}, arith genus gS={gS}")
print(f"nodal geom genus={g_geom_nodal}")
# reducible loci dims
dim_12 = h0_K + h0_K + h0_K2  # (1)+(2): b1 + (c1,c2)
dim_111 = h0_K*3
print(f"reducible (1+2) param dim<={dim_12} codim>={dimB-dim_12}")
print(f"reducible (1+1+1) param dim<={dim_111} codim>={dimB-dim_111}")
assert (h0_K, h0_K2, h0_K3) == (2, 3, 5)
assert dimB == 10 and dimM == 20 and dimM - dimB == 10
assert gS == 10 and g_geom_nodal == 9
assert dimB - dim_12 >= 3 and dimB - dim_111 >= 4
print("ALL CHECKS PASS")
