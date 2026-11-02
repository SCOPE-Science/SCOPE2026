# Universal precanonical Rao profile and spin parity for curves on a line-containing K3

## Finding

Let \(S\subset\mathbb P^5_{\mathbb C}\) be a smooth complete intersection of three quadrics containing a line \(E\). Let \(H\) be its hyperplane divisor and \(D=2H+E\). For an integer \(m\ge1\), let \(C\in|mD|\) be smooth, connected, and disjoint from \(E\); general members have these properties. Write \(\mathcal I_C\) for the ideal sheaf of \(C\) in \(\mathbb P^5\), and let \(t\) range over integers.

**Theorem (precanonical Rao profile).** Every such curve satisfies

\[
h^1(\mathbb P^5,\mathcal I_C(t))=
\begin{cases}
0,&t\le1,\\
\lfloor t^2/4\rfloor,&2\le t\le2m-1,\\
m^2-1,&t=2m.
\end{cases}
\]

Thus the whole positive profile before the canonical twist is independent of the family parameter \(m\), whereas the last twist has an exceptional correction of minus one. These cohomology groups measure precisely the dimensions of the cokernels of the degree-\(t\) ambient-polynomial restriction maps for \(t\ge0\).

**Spin consequence.** The line bundle \(\Theta_m=\mathcal O_C(mH)\) is a theta characteristic, with

\[
h^0(C,\Theta_m)=4m^2+2+\left\lfloor\frac{m^2}{4}\right\rfloor,
\qquad
h^0(C,\Theta_m)\equiv1\pmod2\ \Longleftrightarrow\ m\equiv2\pmod4.
\]

For example, \(m=2\) gives degree \(34\), genus \(69\), defects \((1,2,3)\) in twists \((2,3,4)\), and an odd theta characteristic with \(19\) sections. For \(m=3\), the positive defects through the canonical twist are \((1,2,4,6,8)\) in twists \((2,3,4,5,6)\), and the induced theta characteristic has \(40\) sections and even parity.

## Assumptions and scope

Work over \(\mathbb C\); \(m\) and \(t\) are integers with \(m\ge1\) and \(t\le2m\). A smooth intersection of three quadrics in \(\mathbb P^5\) is a K3 surface, and the line \(E\) is a smooth rational \((-2)\)-curve. Intersection numbers are \(H^2=8\), \(H\cdot E=1\), \(E^2=-2\); hence \(D^2=34\) and \(D\cdot E=0\). By the unprojection morphism of Nasu, \(|D|\) is basepoint-free, contracts precisely \(E\), and general curves in \(|mD|\) avoid \(E\) and are smooth. Their genus is \(g(C)=17m^2+1\), so \(2mH|_C\simeq K_C\) is the canonical twist of the given embedding.

No claim is made for the remaining twists \(t>2m\), the full multiplication structure of the Rao module, arbitrary K3 embeddings, or every curve in the Hilbert component outside the stated smooth locus.

## Proof

**1. Reduction to line bundles on the K3.** Because \(S\subset\mathbb P^5\) is a complete intersection, its homogeneous coordinate ring is arithmetically Cohen--Macaulay. Therefore \(H^1(\mathbb P^5,\mathcal I_S(t))=H^2(\mathbb P^5,\mathcal I_S(t))=0\) for all integers \(t\). Using \(C\sim m(2H+E)\) in the ideal-sheaf exact sequence gives

\[
H^1(\mathbb P^5,\mathcal I_C(t))\simeq
H^1(S,\mathcal O_S((t-2m)H-mE)).
\]

For \(t<2m\), put \(k=2m-t>0\). As \(K_S\simeq\mathcal O_S\), Serre duality identifies the dimensions of the right-hand side with those of \(H^1(S,\mathcal O_S(kH+mE))\).

**2. Exact recursion on the exceptional line.** For \(1\le j\le m\), use the exact sequence

\[
0\longrightarrow\mathcal O_S(kH+(j-1)E)
\longrightarrow\mathcal O_S(kH+jE)
\longrightarrow\mathcal O_E(k-2j)\longrightarrow0.
\]

Kodaira vanishing on the K3 gives \(H^1(S,\mathcal O_S(kH))=0\). For every \(j\ge0\), Serre duality gives \(H^2(S,\mathcal O_S(kH+jE))=0\), since the negative divisor \(-kH-jE\) has negative intersection with the ample divisor \(H\). The restriction degrees \(k-2j\) decrease with \(j\). While they are at least \(-1\), \(H^1(\mathcal O_E(k-2j))=0\) and the intermediate \(H^1\) remains zero. When they reach \(-2\) or below, \(H^0(\mathcal O_E(k-2j))=0\), and the increase in \(h^1\) is exactly \(h^1(\mathbb P^1,\mathcal O(k-2j))=2j-k-1\). Hence

\[
h^1(S,\mathcal O_S(kH+mE))
=\sum_{j=1}^{m}\max\{0,2j-k-1\}
=\sum_{r=0}^{m-1}\max\{0,t-1-2r\}.
\]

For \(t\le1\) all summands vanish. If \(2\le t\le2m-1\), the positive terms form the arithmetic sequence \(t-1,t-3,\ldots\); their sum is \(\lfloor t^2/4\rfloor\). This proves the first two ranges without a genericity restriction beyond the stated smoothness and disjointness.

**3. The canonical endpoint.** For \(t=2m\) the group in Step 1 is \(H^1(S,\mathcal O_S(-mE))\). Serre duality identifies its dimension with \(h^1(S,\mathcal O_S(mE))\). The negative normal bundle \(\mathcal O_E(E)\simeq\mathcal O_{\mathbb P^1}(-2)\) implies, inductively from the restriction sequences, that \(h^0(S,\mathcal O_S(mE))=1\). Also \(h^2(S,\mathcal O_S(mE))=h^0(S,\mathcal O_S(-mE))=0\). K3 Riemann--Roch yields

\[
\chi(S,\mathcal O_S(mE))=2+\frac{(mE)^2}{2}=2-m^2,
\]

so \(h^1(S,\mathcal O_S(mE))=m^2-1\). The endpoint correction arises from this \(\chi(\mathcal O_S)=2\) contribution.

**4. Theta characteristic and section count.** Adjunction and \(C\cap E=\varnothing\) yield

\[
K_C\simeq\mathcal O_C(C)\simeq\mathcal O_C(2mH+mE)
\simeq\mathcal O_C(2mH).
\]

Thus \(\Theta_m=\mathcal O_C(mH)\) is a square root of \(K_C\). From the exact sequence

\[
0\longrightarrow\mathcal O_S(-m(H+E))
\longrightarrow\mathcal O_S(mH)
\longrightarrow\mathcal O_C(mH)\longrightarrow0
\]

and the vanishing \(h^0(S,\mathcal O_S(-m(H+E)))=0\), the cokernel of restriction \(H^0(S,mH)\to H^0(C,\Theta_m)\) has dimension \(h^1(S,-m(H+E))\). By Step 1 with \(t=m\), it equals \(\lfloor m^2/4\rfloor\). Since \(mH\) is ample, K3 Riemann--Roch and Kodaira vanishing give \(h^0(S,mH)=2+4m^2\). The displayed section formula follows. The parity of \(\lfloor m^2/4\rfloor\) is odd precisely when \(m\equiv2\pmod4\), proving the asserted spin parity.

## Verification

The included standalone script `verify_rao.py` checks the intersection form, the exceptional-curve cohomological recurrence, the exact quadratic formula and the special endpoint for all \(1\le m\le64\) and all \(-3\le t\le2m\). It checks the spin dimensions, parity criterion and sample cases. These finite computations do not replace the exact-sequence argument proving the assertions for every \(m\).

## Relationship to prior work

Nasu, *Obstructions to deforming space curves lying on a complete intersection of quadrics* (arXiv:2610.30962v1), supplies the unprojection setting, \(|D|\), and the existence of generically nonreduced Hilbert components for sufficiently large \(m\); the inspected text does not supply the all-twist precanonical Rao profile or the induced theta section count. Ciliberto and Dedieu, *K3 curves with index k>1* (DOI:10.1007/s40574-021-00286-5), study spin curves arising from divisible ample polarizations; their results do not state this exceptional-line Rao profile or its endpoint correction. The displayed identities are derived directly from complete-intersection cohomology and the exceptional-line filtration, rather than claimed as an independent general theorem about K3 or spin moduli.

## Limitations

The profile is proved only through the intrinsic canonical degree \(t=2m\), not in higher twists. It gives the graded dimensions of the Rao module, not its multiplication maps. The spin structure is the naturally induced \(\mathcal O_C(mH)\); not all theta characteristics are classified. Historical priority is provisional because earlier general deficiency-module results may imply this special family. Independent mathematical validation has not been performed. The nonreduced-Hilbert component assertion is used from the cited literature and only in its proven sufficiently-large-\(m\) range.

## References

1. H. Nasu, *Obstructions to deforming space curves lying on a complete intersection of quadrics*, arXiv:2610.30962v1 (first posted 2026-10-22), Theorem 1.1, Lemmas 2.3 and 2.7, §4. https://arxiv.org/html/2610.30962v1
2. C. Ciliberto and T. Dedieu, *K3 curves with index k>1*, Bollettino dell'Unione Matematica Italiana (first published 2021-06-16), DOI:10.1007/s40574-021-00286-5, Introduction §1.4 and §5. https://link.springer.com/article/10.1007/s40574-021-00286-5
