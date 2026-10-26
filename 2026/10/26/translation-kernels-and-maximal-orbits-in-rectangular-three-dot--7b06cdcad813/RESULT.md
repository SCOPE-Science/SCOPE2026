# Translation kernels and maximal orbits in rectangular three-dot shifts

## Finding

Consider the binary Ledrappier three-dot relation \(c_{i,j}+c_{i+1,j}+c_{i,j+1}=0\) on a rectangular torus with periods
\[
m=2^u(2^a-1),\qquad n=2^v(2^b-1),
\]
where \(a,b\geq1\) and \(u,v\geq0\) are integers. Put \(g=\gcd(a,b)\), \(r=2^{\min(u,v)}\), and \(L=r(2^g-1)\). Write \(\mathcal P_{m,n}\) for the finite group of configurations.

The dual \(\mathbb F_2[\mathbb Z^2]\)-module of this finite action is explicitly \(Q_{g,r}=\mathbb F_2[X]/(H_g(X)^r)\), with horizontal and vertical multipliers \(X\) and \(1+X\), where \(H_g(X)=1+X+\cdots+X^{2^g-2}\). Thus **rectangles having the same \(g\) and \(r\) support linearly equivariantly isomorphic configuration systems**, even if their actual side lengths differ.

If \(g=1\), it consists of the zero configuration only. If \(g\geq2\), then
\[
|\mathcal P_{m,n}|=2^{r(2^g-2)},
\]
and horizontal and vertical translation each have permutation order exactly \(L\) on \(\mathcal P_{m,n}\). The joint translation representation factors through \((\mathbb Z/L\mathbb Z)^2\). Its kernel is
\[
\ker\rho=\begin{cases}
\{(0,0)\}, &g\geq3,\\
\{(0,0),(r,r),(2r,2r)\},&g=2,
\end{cases}
\]
where coordinates are taken modulo \(L\). In each nontrivial case some configuration has stabilizer *exactly* this kernel; thus the largest translation-orbit size is \(L^2\) for \(g\geq3\), and \(L^2/3\) for \(g=2\). Equivalently, the faithful image of the translation group is respectively \((\mathbb Z/L\mathbb Z)^2\) or \(\mathbb Z/(3r)\mathbb Z\times\mathbb Z/r\mathbb Z\).

The point-count identity is classical in the broader algebraic periodic-point framework; the assertion of interest here is the **explicit equivariant linear type**, the sharp **joint translation kernel and exceptional degree-two case**, and the **attainment of the maximal orbit by one configuration**.

## Assumptions and scope

All vector spaces, polynomial rings and configuration arrays are over \(\mathbb F_2\). All torus indices are interpreted cyclically. The action of \((s,t)\in\mathbb Z^2\) is \((\rho(s,t)c)_{i,j}=c_{i+s,j+t}\). This is an assertion about these rectangular finite subsystems, not the global automorphism group of the infinite shift. The parameters \(a,b,u,v\) are arbitrary within the displayed ranges; the formulas include \(r=1\), \(g=1\), unequal periods, and arbitrarily large powers of two.

## Proof

**1. The exact finite dual module.** Pontryagin duality (equivalently, the transpose of the linear defining equations) identifies the character group of \(\mathcal P_{m,n}\) with
\[
R_{m,n}=\frac{\mathbb F_2[X,Y]}{(1+X+Y,\ X^m+1,\ Y^n+1)}
\cong\frac{\mathbb F_2[X]}{(\gcd(X^m+1,(1+X)^n+1))}.
\]
Horizontal and vertical translations dualize to multiplication by \(X\) and \(1+X\), respectively. Let \(q=2^g\), \(\ell=q-1\), and \(H_g(X)=1+X+\cdots+X^{q-2}=(X^\ell+1)/(X+1)\).

The roots of \(X^{2^a-1}+1\) are exactly \(\mathbb F_{2^a}^{\times}\), and those of \((1+X)^{2^b-1}+1\) are exactly \(\mathbb F_{2^b}\setminus\{1\}\). Their intersection is \(\mathbb F_q\setminus\{0,1\}\), since \(\mathbb F_{2^a}\cap\mathbb F_{2^b}=\mathbb F_{2^g}\). Both polynomials are squarefree, and Frobenius powers give root multiplicities \(2^u\) and \(2^v\). Consequently their gcd is \(H_g(X)^r\), and
\[
R_{m,n}\cong Q_{g,r}:=\mathbb F_2[X]/(H_g^r).
\]
For \(g=1\), \(H_1=1\) and the module is zero. Otherwise the vector-space dimension is \(r(q-2)\), proving the claimed number of configurations. Because \(H_g(0)=H_g(1)=1\), both multipliers \(X\) and \(X+1\) are units in \(Q_{g,r}\).

**2. Orders of the two generators.** The polynomial identities
\[
X^\ell+1=(X+1)H_g,\qquad (X+1)^\ell+1=XH_g
\]
follow from \(\ell=q-1\) and \((X+1)^q=X^q+1\). Raising them to the \(r\)-th power shows \(X^{\ell r}=(X+1)^{\ell r}=1\) in the quotient. A primitive element of \(\mathbb F_q^\times\setminus\{1\}\), which exists for \(g\geq2\), shows that either order is divisible by \(\ell\). Further, for any \(2^h<r\), the difference \(X^{\ell 2^h}+1=(X+1)^{2^h}H_g^{2^h}\) is nonzero modulo \(H_g^r\), and similarly for \(X+1\). Thus each exact order is \(L=\ell r\). Since \(g\mid a,b\) and \(r\mid2^u,2^v\), we have \(L\mid m,n\), so the specified quotient action is legitimate.

**3. Relations modulo the squarefree factor.** Suppose \(X^s(X+1)^t=1\) modulo \(H_g\), where exponents may be reduced modulo \(\ell\). Equivalently,
\[
\lambda^s(1+\lambda)^t=1\quad\text{for every }\lambda\in\mathbb F_q\setminus\{0,1\}.
\]
Apply first the bijection \(\lambda\mapsto\lambda^{-1}\), then \(\lambda\mapsto1+\lambda\), and compare each transformed identity with the original. Because both \(\lambda\) and \(\lambda/(1+\lambda)\) range over primitive elements, this gives
\[
2s+t\equiv0\pmod\ell,\qquad s-t\equiv0\pmod\ell.
\]
Hence \(s\equiv t\) and \(3s\equiv0\) modulo \(\ell\). If \(g\) is odd, \(3\nmid\ell\), so \(s\equiv t\equiv0\). If \(g\geq4\) is even, the two possible nonzero diagonal residues would force \([\lambda(1+\lambda)]^{\ell/3}=1\) for all \(q-2\) admissible elements. The nonzero polynomial \([X(X+1)]^{\ell/3}+1\) has degree \(2\ell/3<q-2\) for \(q\geq16\), a contradiction. Thus the semisimple kernel is trivial whenever \(g\geq3\). For \(g=2\), \(H_2=X^2+X+1\) and \(X(X+1)=1\) modulo \(H_2\); its semisimple kernel is exactly \(s\equiv t\pmod3\).

**4. The nilpotent thickening does not add relations.** For \(g\geq3\), step 3 forces \(s=\ell S\), \(t=\ell T\) with \(S,T\) modulo \(r\). Step 2 yields
\[
X^s(X+1)^t=(1+(X+1)H_g)^S(1+XH_g)^T.
\]
If \((S,T)\not\equiv(0,0)\pmod r\), let \(2^h\) be the minimum power of two dividing either nonzero residue. The lowest possible nonzero coefficient of \(H_g\), at exponent \(2^h<r\), reduces modulo \(H_g\) to exactly one of \(X+1\), \(X\), or \(1\), raised to \(2^h\). Each is a unit modulo \(H_g\), so this product is not \(1\) modulo \(H_g^r\). The joint kernel is therefore trivial.

For \(g=2\), the semisimple condition gives \(s=t+3K\) modulo \(3r\). Use \(X^3=1+(X+1)H_2\) and \(X(X+1)=1+H_2\) to write
\[
X^s(X+1)^t=(1+(X+1)H_2)^K(1+H_2)^t.
\]
Unless \(r\mid K\) and \(r\mid t\), its first potentially nonzero \(H_2^{2^h}\) coefficient is one of \(X+1\), \(1\), or \(X\) raised to \(2^h\), again a unit modulo \(H_2\). Thus \(K\equiv t\equiv0\pmod r\), implying \(s=t\pmod{3r}\) with \(t\in\{0,r,2r\}\). Conversely these three relations hold because \((X(X+1))^r=(1+H_2)^r=1\) modulo \(H_2^r\). This proves the exceptional kernel formula. The quotient of \((\mathbb Z/(3r))^2\) by this diagonal order-three subgroup is \(\mathbb Z/(3r)\times\mathbb Z/r\), since \(r\) is a power of two.

**5. One configuration realizes the faithful image.** Let \(d=\deg(H_g^r)>0\), identify each element of \(Q_{g,r}\) with its unique representative of degree less than \(d\), and define the \(\mathbb F_2\)-linear functional \(\varphi(f)=[X^{d-1}]f\). For every nonzero residue \(z\) of degree \(k<d\), choose \(f=X^{d-1-k}\). Then \(\varphi(zf)=1\). Thus the bilinear pairing \((z,f)\mapsto\varphi(zf)\) is nondegenerate. An element of the translation group fixes \(\varphi\) under the dual action precisely if \(\varphi((X^s(X+1)^t-1)f)=0\) for every \(f\), which by nondegeneracy is equivalent to \(X^s(X+1)^t=1\) in \(Q_{g,r}\). Therefore this character, viewed as an actual configuration by biduality, has stabilizer exactly the global kernel. Orbit–stabilizer proves the maximal orbit-size assertions.

## Verification

The companion verifier `verify.py` implements binary polynomial gcds, finite-torus linear algebra, explicit translation multipliers, and the dual functional witness. Running `python3 verify.py` from the package prints:

```text
VERIFY_OK polynomial_cases=196 physical_rank_cases=94 kernel_cases=40 full_orbit_witness_cases=35 additional_rank_cases=7
```

The parameter tests include degenerate \(g=1\), nonsquare rectangles, repeated-root factors and nontrivial kernels. They are finite independent corroboration, not a replacement for the preceding unrestricted proof.

## Relationship to prior work

Ledrappier's three-dot action is classical. Miles and Ward's `arxiv:1411.5295` treats directional periodicity and this action. Their `arxiv:1504.04973`, particularly Example 4.1 and its surrounding general algebraic point-count machinery, studies counts of periodic points for finite-index subgroups and expressly includes the square-period count. Those sources establish stronger **general counting frameworks** than the numerical count stated here; the count is given only to normalize the finite subsystem, and is not claimed as new. The distinct assertion tested against them is an explicit group-level joint translation kernel, including its exceptional order-three case for \(g=2\), and an explicit maximal-orbit witness on every stated subsystem. The general subgroup-count formulas might also allow these conclusions by further extraction; this is a priority risk, not evidence of independence.

## Limitations

This theorem concerns periods \(m=2^u(2^a-1)\), \(n=2^v(2^b-1)\), not arbitrary positive periods. It classifies the kernel of the joint translation action and the largest attainable orbit, not the counts of every orbit size. It does not establish historical priority. Lind's earlier 1996 account of higher-rank dynamical zeta functions is particularly relevant but its full text was inaccessible, so direct theorem-level coverage there remains unresolved. The present finite verifier checks only the bounded parameter ranges stated above.

## References

- R. Miles and T. Ward, *Directional uniformities, periodic points, and entropy*, arXiv:1411.5295, first posted 2014-11-19; especially discussion of Ledrappier's example.
- R. Miles and T. Ward, *The dynamical zeta function for commuting automorphisms of zero-dimensional groups*, arXiv:1504.04973, first posted 2015-04-20; especially Section 4, Example 4.1, and general periodic-point formulas.
- F. Ledrappier, *Un champ markovien peut être d'entropie nulle et mélangeant*, C. R. Acad. Sci. Paris (1978); original model, cited through the preceding sources.
- D. Lind, *A zeta function for \(\mathbb Z^d\)-actions* (1996); mentioned for contextual priority, full text not inspected.
