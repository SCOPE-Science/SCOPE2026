# Exact zeta function and Newton polygon of the six-rational-branch Humbert–Edge curve over \\(\\mathbf F_5\\)

## Finding
Let \\(X\\subset\\mathbf P^5_{\\mathbf F_5}\\) have homogeneous coordinates \\([U_0:U_1:U_2:U_3:U_4:Z]\\) and be cut out by the four diagonal quadrics
\\[
U_i^2-U_0^2+iZ^2=0,\\qquad i\\in\\{1,2,3,4\\}.
\\]
Then \\(X\\) is a smooth geometrically connected genus-\\(17\\) curve. Its deck quotient \\(X\\to\\mathbf P^1\\), given by \\(t=U_0^2/Z^2\\), has Galois group \\((\\mathbf Z/2\\mathbf Z)^5\\) and is branched precisely at all six points of \\(\\mathbf P^1(\\mathbf F_5)\\).

The exact Hasse–Weil numerator is
\\[
L_X(T)=(1-2T+5T^2)^5(1+2T+5T^2)^{10}(1-5T^2)^2.
\\]
Thus \\(Z(X/\\mathbf F_5,T)=L_X(T)/((1-T)(1-5T))\\). The geometric Jacobian has \\(5\\)-rank \\(15\\), \\(a\\)-number \\(2\\), and Newton slopes \\(0\\) with multiplicity \\(15\\), \\(1/2\\) with multiplicity \\(4\\), and \\(1\\) with multiplicity \\(15\\). In particular, the curve has precisely \\(16\\) rational points over \\(\\mathbf F_5\\), precisely \\(96\\) over \\(\\mathbf F_{25}\\), and precisely \\(16\\) over \\(\\mathbf F_{125}\\).

## Assumptions and scope
All finite fields are of characteristic \\(5\\). The curve is the **specified split diagonal complete intersection**; no uniqueness statement is made for its quadratic twists or for other six-point covers. Counts refer to projective smooth curves, not coordinate classes. The cover group has order \\(32\\), prime to the characteristic; this is crucial for the cohomological and Cartier decompositions.

## Proof
**Smoothness, connectedness, and branch data.** On the chart \\(Z=1\\), put \\(u_i=U_i/Z\\); the equations become \\(u_i^2=t-i\\) for \\(i=0,1,2,3,4\\), with \\(t=u_0^2\\). The five square classes of \\(t-i\\) in \\(\\overline{\\mathbf F}_5(t)^*/\\overline{\\mathbf F}_5(t)^{*2}\\) are independent: valuation at the corresponding distinct roots detects every coefficient of a prospective relation. The function field therefore has degree \\(32\\) and is geometrically connected. Each of the five finite branch points has inertia order \\(2\\), and infinity also has inertia order \\(2\\), because all five radicands have odd degree. It has no other branch points.

For completeness, the four defining quadrics form a smooth complete intersection. On \\(Z=1\\) at most one of the five coordinates \\(u_0,\\ldots,u_4\\) can vanish, since their squares are distinct. If \\(u_0=0\\), the other four partial derivatives \\(2u_i\\) provide rank four; if \\(u_j=0\\) for \\(j>0\\), then \\(u_0\\neq0\\) and the other three \\(2u_i\\) together with the derivative in \\(u_0\\) provide rank four. If none vanish, all four diagonal partial derivatives provide rank four. On \\(Z=0\\), all \\(U_i^2=U_0^2\\) and \\(U_0\\neq0\\), so the four derivatives in \\(U_1,\\ldots,U_4\\) are nonzero and independent. Riemann–Hurwitz now gives
\\[
2g(X)-2=32(-2)+6\\cdot16=32,
\\]
so \\(g(X)=17\\).

**Character decomposition.** The independent sign changes of \\(u_0,\\ldots,u_4\\) form a group \\(G\\cong(\\mathbf Z/2\\mathbf Z)^5\\). For each nonempty subset \\(S\\subseteq\\{0,1,2,3,4\\}\\), let \\(C_S\\) be the smooth projective model of
\\[
y^2=\\prod_{i\\in S}(t-i).
\\]
The quotient corresponding to the sign character indexed by \\(S\\) is \\(C_S\\). Since \\(|G|=32\\) is invertible in characteristic \\(5\\), character idempotents yield an \\(\\mathbf F_5\\)-defined prime-to-\\(5\\) isogeny decomposition of Jacobians and Frobenius representations. The degree-\\(k\\) double cover has genus \\(\\lfloor(k-1)/2\\rfloor\\). The five subsets of size one and ten of size two contribute genus zero; the ten of size three and five of size four each contribute an elliptic factor; and the one subset of size five contributes the genus-two curve \\(C_*:y^2=t^5-t\\). Thus the total genus is \\(10+5+2=17\\), and every eigenvalue of Frobenius is accounted for.

**Elliptic Frobenius traces.** Each of the fifteen elliptic factors is a double cover of \\(\\mathbf P^1\\) branched at four distinct \\(\\mathbf F_5\\)-rational points, including infinity for odd-degree models. Accordingly it has all four two-torsion points rational, so its cardinality over \\(\\mathbf F_5\\) is divisible by \\(4\\). The Hasse bound forces this cardinality to be either \\(4\\) or \\(8\\), and its trace is respectively \\(2\\) or \\(-2\\). Directly from the defining equations, the only points of \\(X\\) over \\(\\mathbf F_5\\) are the sixteen points at infinity \\(Z=0\\): at a finite value \\(t\\in\\mathbf F_5\\), the five radicands \\(t-i\\) include both nonsquare values \\(2\\) and \\(3\\), so cannot all be squares. Moreover \\(C_*(\\mathbf F_5)\\) consists of its five finite branch points and the point at infinity, so has \\(6\\) points and trace zero. Consequently the sum of the fifteen elliptic traces is \\(5+1-16=-10\\). If \\(n_+\\) and \\(n_-\\) count the traces \\(2\\) and \\(-2\\), then \\(n_++n_-=15\\) and \\(2n_+-2n_-=-10\\), so \\(n_+=5\\) and \\(n_-=10\\).

**Genus-two factor.** For any \\(t\\in\\mathbf F_{25}\\), set \\(r=t^5-t\\). Then \\(r^5=-r\\). If \\(r\\neq0\\), we have \\(r^4=-1\\) and hence \\(r^{12}=-1\\), so \\(r\\) is not a square in \\(\\mathbf F_{25}\\). The only finite rational points of \\(C_*\\) lie above the five values \\(t\\in\\mathbf F_5\\) where \\(r=0\\); together with infinity, this yields \\(\\#C_*(\\mathbf F_{25})=6\\). Thus the Frobenius traces in degrees \\(1\\) and \\(2\\) are respectively \\(0\\) and \\(25+1-6=20\\). The Weil eigenvalues have complex absolute value \\(\\sqrt5\\), so equality in the triangle inequality for their squares forces all four eigenvalue squares to equal \\(5\\). Therefore \\(L_{C_*}(T)=(1-5T^2)^2\\). Combining it with the elliptic factors proves the displayed zeta function for all finite extensions, not merely the first three.

**Newton polygon and \\(a\\)-number.** The elliptic factors have trace \\(\\pm2\\not\\equiv0\\pmod5\\), so all fifteen are ordinary. For \\(C_*\\), the Cartier–Manin matrix of the genus-two curve vanishes: in characteristic \\(5\\),
\\[
(t^5-t)^{(5-1)/2}=t^{10}-2t^6+t^2,
\\]
whose coefficients at exponents \\(5i-j\\) for \\(1\\le i,j\\le2\\), namely \\(3,4,8,9\\), all vanish. Thus \\(C_*\\) has \\(a\\)-number \\(2\\), and its Jacobian is superspecial. The order-\\(32\\) quotient decomposition is prime to \\(5\\), so it preserves the \\(5\\)-divisible groups and their \\(a\\)-numbers. Summing fifteen ordinary elliptic factors and a superspecial genus-two factor yields the stated \\(5\\)-rank, \\(a\\)-number, and Newton slopes.

## Verification
The standalone exact-arithmetic program `verify.py` enumerates points of the explicitly defined multiquadratic cover over \\(\\mathbf F_5\\), \\(\\mathbf F_{25}\\), and \\(\\mathbf F_{125}\\); enumerates the genus-two quotient over the first two fields; checks all fifteen elliptic traces directly; checks the Cartier–Manin exponent list; and independently matches the zeta numerator's predicted point counts. Run it with `python3 verify.py` (Python standard library only). Observed output ends with `VERIFY_OK` and gives \\(16,96,16\\) points on \\(X\\). Finite-field enumeration supports, but does not replace, the symbolic all-extension argument above.

## Relationship to prior work
Auffarth–Lucchini Arteche–Rojas prove the general Humbert–Edge Jacobian decomposition (2019 preprint, 2020 revision), which covers the existence of the elliptic and genus-two factors and is **not** claimed as new here. Castorena–Frías-Medina (2021) describe type-five Humbert–Edge curves, their six branch points, and the genus-two/Kummer correspondence, primarily over the complex numbers. Martínez-Núñez (2023) provides a more general Fermat-curve Jacobian decomposition. The specific complete \\(\\mathbf F_5\\)-rational branch configuration, exact arithmetic over every finite extension, explicit Frobenius factor multiplicities, and the resulting \\(5\\)-rank and \\(a\\)-number are the claim at issue. Targeted checks of these papers, exact equations, aliases, and published mathematical-result records disclosed no identical arithmetic assertion; an unindexed specialized calculation cannot be ruled out.

## Limitations
This is one explicit split model, not a classification of all genus-seventeen Humbert–Edge curves in characteristic five, and not a classification of twists. It proves exact arithmetic for this model, without claiming any novelty for the general group-theoretic decomposition, the definition of the family, or the classical genus-two curve separately. Independent validation has not been performed.

## References
1. R. Auffarth, G. Lucchini Arteche and A. M. Rojas, *A decomposition of the Jacobian of a Humbert-Edge curve*, arXiv:1905.12690v2, Theorem 2.1 (first publicly submitted 2019-05-29), https://arxiv.org/abs/1905.12690.
2. A. Castorena and J. B. Frías-Medina, *Geometric aspects on Humbert-Edge’s curves of type 5, Kummer surfaces and hyperelliptic curves of genus 2*, arXiv:2106.00813v1, Sections 3.1 and 3.3 (2021-06-01), https://arxiv.org/abs/2106.00813.
3. G. Martínez-Núñez, *Decomposition of jacobians of generalized Fermat curves*, arXiv:2303.18056v1 (2023-03-31), https://arxiv.org/abs/2303.18056.
