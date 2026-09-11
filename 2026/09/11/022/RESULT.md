# Low-quotient-degree exclusion for the (2,10,4) general-determinant locus on general genus-6 curves

## Context
Fixed-determinant higher-rank Brill–Noether theory asks which triples
$(g,d,k)$ occur for general versus special determinant. At
$(g,d,k)=(6,10,4)$ the canonical locus $B(2,K_C,4)$ is known nonempty of
dimension 5 (Bertram–Feinberg–Mukai), while the fixed-general-determinant
expected number is $\rho=3g-3-k(k-d+2g-2)=15-16=-1$, predicting emptiness
of the general fibre. The full emptiness of $B(2,M,4)$ for general $M$ is
open; this record banks the low-quotient-degree reduction.

## Definitions
- $C$: general (Petri-general, Clifford index 2, gonality 5) smooth
  genus-6 curve; line-bundle loci $W^r_d(C)$ empty if
  $\rho(g,r,d)=g-(r+1)(g-d+r)<0$, of pure dimension $\rho$ if $\rho\ge0$.
- $M$: general point of $\mathrm{Pic}^{10}(C)$ ($\dim 6$); rank-2
  degree-10 bundles have $\chi=10-12+2=0$, slope $\mu=5$.
- $B(2,M,4)$: stable rank-2 $E$ with $\det E=M$, $h^0(C,E)\ge4$.
- Every line-quotient presentation is $0\to N\to E\to L\to0$ with
  $\deg L=e$, $N=M\otimes L^{-1}$ of degree $10-e$.

## Result
Let $C$ be general genus-6 and $M$ general in $\mathrm{Pic}^{10}(C)$.
There is no stable rank-2 $E$ with $\det(E)=M$ and $h^0(C,E)\ge4$
admitting a line-bundle quotient $L$ of degree $e\le6$. Hence the
low-quotient-degree stratum of $B(2,M,4)$ is empty, and any putative
counterexample to full emptiness has minimal quotient degree $\ge7$.

## Proof / evidence
Stability floor: $\mu(E)=5$ forces every line subbundle to have degree
$\le4$, so every line quotient has degree $\ge6$; strata $e\le5$ are
empty with no genericity hypothesis.

Degree 6: $\deg N=4$, $\deg L=6$, and $h^0(E)\ge4$ implies
$h^0(N)+h^0(L)\ge4$ via $0\to H^0(N)\to H^0(E)\to H^0(L)$.
$h^0(L)\ge4$ needs $W^3_6\ne\emptyset$ but $\rho(6,3,6)=-6$ (empty);
$h^0(N)\ge3$ needs $W^2_4\ne\emptyset$ but $\rho(6,2,4)=-6$ (empty).
So $h^0(N)\le2$, $h^0(L)\le3$, leaving:
$(n_0\ge1,\ell_0\ge3)$ on $W^0_4\times W^2_6$ of dimension $4+0=4$
($\rho(6,0,4)=4$, $\rho(6,2,6)=0$);
$(n_0\ge2,\ell_0\ge2)$ on $W^1_4\times W^1_6$ of dimension $0+4=4$
($\rho(6,1,4)=0$, $\rho(6,1,6)=4$).
Each incidence maps $(N,L)\mapsto N\otimes L$ to the 6-fold
$\mathrm{Pic}^{10}(C)$ with image dimension $\le4<6$; general $M$ lies
outside every image. Thus no $(N,L)$ over general $M$ meets
$h^0(N)+h^0(L)\ge4$, so the $M$-fibre extension family and its Porteous
coboundary locus are empty a fortiori. This certifies every residual
$e\le6$ empty with no dominating component.

## Limitations
- General $C$ and general $M$ throughout; nothing claimed for special
  curves (plane quintics, trigonal) or special determinants (canonical
  $B(2,K,4)$ is nonempty).
- Stable bundles only.
- Quotient degrees $e\ge7$ untouched; the degree-7 incidence
  ($\dim W^0_3+\dim W^2_7=3+3=6=\dim\mathrm{Pic}^{10}$) can dominate, so
  full $B(2,M,4)$ emptiness remains open.

## Reproducibility
`output/artifacts/verify_counts.py` (stdlib only) replays the full
$\rho$-table, the stability floor, and both incidence dimensions,
ending in `VERIFY_OK`.

## References
- M. Teixidor i Bigas, Existence of vector bundles of rank two with
  fixed determinant and sections, arXiv:1007.2308v1.
- H. Lange, P. E. Newstead, V. Strehl, Non-emptiness of Brill-Noether
  loci in $M(2,L)$, arXiv:1312.1844v4.
- I. Grzegorczyk, V. Mercat, P. E. Newstead, Stable bundles of rank 2
  with 4 sections, arXiv:1006.1258v3.
- P. E. Newstead, Some examples of rank-2 Brill–Noether loci, Rev. R.
  Acad. Cienc. Exactas Fís. Nat. Ser. A Mat. (2017),
  doi:10.1007/s13163-017-0241-6.
- B. Osserman, Brill–Noether loci with fixed determinant in rank 2,
  doi:10.1142/S0129167X13500997; Special determinants in higher-rank
  Brill–Noether theory, doi:10.1142/S0129167X13500845.
