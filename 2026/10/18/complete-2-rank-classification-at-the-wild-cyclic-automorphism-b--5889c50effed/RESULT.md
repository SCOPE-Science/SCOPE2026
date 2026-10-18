# Complete \(2\)-rank classification at the wild cyclic automorphism boundary

## Finding

Let \(k\) be algebraically closed of characteristic \(2\), let \(C/k\) be a smooth projective connected curve of genus \(g\ge2\), and suppose it carries a specified cyclic group \(G\cong C_{2g}\) of automorphisms. Write \(\gamma(C)\) for the \(2\)-rank defined by \(|\operatorname{Jac}(C)[2](k)|=2^{\gamma(C)}\). Then
\[
\boxed{\gamma(C)\in\{0,1\},\qquad\gamma(C)=1\iff (C,G)\text{ belongs to the two-wild-branch family}.}
\]
Explicitly, the unique positive-rank family comprises exactly the pairs represented by
\[
y^2+y=c(x^m+x^{-m}),\qquad m\ge3\text{ odd},\quad c\in k^\times,\quad g=m,\quad G\cong C_{2m}.
\]
The complete remaining four families of the Kazemifard–Tafazolian wild-boundary classification have rank zero:

| Group order | Genus | Normal form or quotient data | \(\gamma(C)\) |
| ---: | ---: | --- | ---: |
| \(6\) | \(3\) | \(w^3=z(z-1),\ y^2+y=az\) | **0** |
| \(30\) | \(15\) | \(w^{15}=z^3(z-1)^5,\ y^2+y=az\) | **0** |
| \(4\) | \(2\) | One-branched cyclic-four Artin–Schreier–Witt cover | **0** |
| \(12\) | \(6\) | Cyclic-four Witt cover combined with \(x^3=z\) | **0** |

For every row, the nonzero coefficient \(a\) in the stated Artin–Schreier equation is arbitrary. The result covers all parameters of the two Witt families. In particular no wild cyclic-boundary curve in characteristic two is ordinary, and among them the exact positive-rank locus has rank one in unbounded genus.

## Assumptions and scope

All models refer to smooth projective normalizations of function fields. In characteristic two the boundary order \(2g-1\) is odd, hence automatically tame; the wild boundary is exactly \(N=2g\). The list of five pairs is imported from Kazemifard–Tafazolian, Theorem 6.1 and Table 1 (arXiv:2610.04702v1). Their classification includes precisely the two-pole family and the four one-wild-branch families above. No claim about uniqueness of the cyclic group, the full automorphism group, or other characteristics is part of this theorem.

## Proof

For any Galois \(p\)-group cover \(V\to W\) of degree \(q\), the Deuring–Shafarevich formula is
\[
\gamma(V)-1=q(\gamma(W)-1)+\sum_{O}(q-|O|),
\]
where the sum runs over short orbits of the group on \(V\). In an Artin–Schreier cover of the rational line with exactly \(r\) reduced poles, every pole has one totally ramified point, so \(\gamma=(p-1)(r-1)\). If \(V\to W\) is an Artin–Schreier cover with exactly one pole, \(\gamma(V)=p\gamma(W)\). A cyclic-four cover of \(\mathbb P^1\) with just one totally ramified orbit has \(\gamma-1=4(-1)+(4-1)=-1\), so \(\gamma=0\).

For \(y^2+y=c(x^m+x^{-m})\), the two distinct reduced poles at zero and infinity each have order \(m\), which is odd, so the first formula gives \(\gamma=1\) for every \(m\ge3\) odd.

For \(G=C_6\) and genus three, the tame Kummer quotient \(Y=C/C_2\) is \(w^3=z(z-1)\). It is also described by \(z^2+z=w^3\): a single-pole Artin–Schreier cover of \(\mathbb P^1_w\), so \(\gamma(Y)=0\). The Artin–Schreier double cover \(C\to Y\), defined by \(y^2+y=az\), has only one pole over infinity, hence \(\gamma(C)=2\gamma(Y)=0\).

For \(G=C_{30}\) and genus fifteen, the tame Kummer quotient \(Y=C/C_2\), with equation \(w^{15}=z^3(z-1)^5\), has genus four. Put \(u=w^6/[z(z-1)^2]\) and \(v=w/u\); then \(u^5=z\), \(v^3=z-1\), and \(Y\) is birational to
\[
v^3=u^5-1.
\]
A basis of regular differentials is
\[
\omega_0=du/v,\quad \omega_1=du/v^2,\quad \omega_2=u\,du/v^2,\quad \omega_3=u^2\,du/v^2.
\]
To see regularity, at a finite branch point \(v\) has valuation one and \(du\) valuation two, and at the unique point at infinity \(u,v,du\) have valuations \(-3,-5,-4\), respectively. Each displayed differential is regular; their number equals the genus. In characteristic two, the Cartier operator satisfies
\[
\mathcal C(\omega_0)=\omega_3,\qquad\mathcal C(\omega_2)=\omega_0,\qquad\mathcal C(\omega_1)=\mathcal C(\omega_3)=0.
\]
Indeed \(v^3=u^5+1\). The identity \(\mathcal C(R(u)\,du)=\sqrt{R'(u)}\,du\) with \(R=1/(u^5+1)\), together with semilinearity, gives \(\mathcal C(du/v)=u^2du/v^2\). The other cases follow from \(\mathcal C(u^{2h+1}du)=u^hdu\) and \(\mathcal C(u^{2h}du)=0\). Thus \(\mathcal C^3=0\) and \(\gamma(Y)=0\). The pullback Artin–Schreier double cover \(C\to Y\) has exactly one pole, since the function \(z\) has a unique pole at infinity on the Kummer curve. Consequently \(\gamma(C)=2\gamma(Y)=0\).

Finally, for \(G=C_4\) and genus two, the cyclic-four Witt model gives a degree-four cover of \(\mathbb P^1\) with exactly one totally ramified orbit, so the cyclic-four Deuring–Shafarevich calculation above gives rank zero. The \(G=C_{12}\) genus-six Witt model has a Sylow-four subgroup whose quotient is the rational curve \(x^3=z\), again with one totally ramified orbit, so it also has rank zero. The five families are exhaustive, completing both directions of the classification.

## Verification

The standalone Python script `verify.py` uses exact prime-field matrices to check that the displayed genus-four Cartier operator has nilpotence index three, and independently counts the points of \(v^3=u^5+1\) over \(\mathbb F_{2^r}\) for \(r=1,2,3,4\), obtaining \((3,5,9,9)\). Newton identities then give initial zeta numerator coefficients \((1,0,0,0,-2)\), consistent with rank zero. It also checks the one-branch cyclic-four identity. The full theorem rests on the symbolic argument and the exhaustive source classification, not on finite experiments.

## Relationship to prior work

Kazemifard–Tafazolian, *Cyclic automorphisms beyond the canonical bound* (arXiv:2610.04702v1), classify the wild-boundary pairs by genus, group order, and ramification. They do not report this characteristic-two \(2\)-rank classification. Their later paper *Artin–Schreier Curves of Prescribed \(p\)-Rank Without Extra Automorphisms* (arXiv:2610.13279v1) treats odd-characteristic rational-base covers, so does not furnish the higher-genus characteristic-two Kummer quotient calculation. Timpanella (arXiv:2609.34709v1) classifies larger cyclic orders \(N\ge2g+1\), outside the present boundary. Individual old cyclic-four parameter, cyclic-twelve isomorphism, or characteristic-two related Kummer-rank calculations are not claimed as new. The contribution is the sharp complete five-family \(2\)-rank classification and its genus-four Cartier step.

## Limitations

Only characteristic two and the wild cyclic subgroup order \(2g\) are covered. The result assumes the correctness and completeness of the cited group-action classification. Rank zero does not imply supersingular Jacobians; Newton polygons, \(a\)-numbers, full automorphism groups, and tame actions remain outside scope. The Deuring–Shafarevich formula and the Artin–Schreier two-pole formula are classical. Earlier unindexed coverage remains a historical priority risk, and no independent verification has been performed.

## References

1. A. Kazemifard and S. Tafazolian, *Cyclic automorphisms beyond the canonical bound*, arXiv:2610.04702v1 (2026-10-03), especially Proposition 5.3, Proposition 5.5, Theorems 5.7–5.8 and 6.1, and Table 1. https://arxiv.org/html/2610.04702v1
2. S. Tafazolian and A. Kazemifard, *Artin–Schreier Curves of Prescribed p-Rank Without Extra Automorphisms*, arXiv:2610.13279v1 (2026-10-09), Proposition 2.1. https://arxiv.org/html/2610.13279v1
3. M. Timpanella, *Large cyclic automorphism groups and cyclic subgroups of index two in characteristic two*, arXiv:2609.34709v1 (2026-09-28), treats order at least \(2g+1\).
4. D. Shiomi, *On the Deuring-Shafarevich Formula*, Tokyo J. Math. 34 (2011), DOI:10.3836/tjm/1327931387.
