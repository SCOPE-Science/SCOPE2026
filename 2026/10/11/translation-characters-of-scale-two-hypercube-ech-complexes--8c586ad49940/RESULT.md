# Translation characters of scale-two hypercube Čech complexes

## Finding

Let \(Q_n\) denote the \(n\)-dimensional cube graph on \(V=\mathbb F_2^n\), for every integer \(n\ge 2\). Let \(K_n=\mathcal N(Q_n,2)\) be its intrinsic graph Čech complex at scale \(2\), the nerve of the closed radius-one balls in the geometric realization of \(Q_n\). Coordinate translations \(a\in T_n=\mathbb F_2^n\) act simplicially on \(K_n\).

The only nonzero positive-degree rational homology is in degree \(2\), of dimension
\[
\beta_n=2^{n-2}(n^2-3n+4)-1.
\]
For \(a\ne0\), the trace on \(H_2(K_n;\mathbb Q)\) is
\[
\operatorname{tr}(a)=\begin{cases}2^{n-1}-1,&\operatorname{wt}(a)\in\{1,2\},\\-1,&\operatorname{wt}(a)\ge3.\end{cases}
\]
The identity has trace \(\beta_n\). In particular, the **complete rational translation-module decomposition** is
\[
H_2(K_n;\mathbb Q)\cong\bigoplus_{S\subseteq[n]}m_{n,|S|}\,\mathbb Q_{\chi_S},\qquad \chi_S(a)=(-1)^{\sum_{i\in S}a_i},
\]
with exact multiplicities
\[
m_{n,k}=\begin{cases}\binom n2,&k=0,\\\binom n2+1-k(n+1-k),&1\le k\le n.\end{cases}
\]
In particular, the invariant subspace has dimension \(\binom n2\), and for every \(n\ge4\) all \(2^n\) translation characters occur with positive multiplicity.

## Assumptions and scope

The cubes are **graphs** with unit-length edges and shortest-path metric on the geometric realizations; this is not a Euclidean Čech complex. The input Čech scale is \(r=2\), so its metric-ball radius is \(r/2=1\). Its simplices are precisely the nonempty subsets of a closed graph neighborhood
\[
N[v]=\{v,v+e_1,\ldots,v+e_n\},\qquad v\in\mathbb F_2^n,
\]
by Lemma 3.1 of Adams--Shukla--Singh. The space \(\mathbb Q_{\chi_S}\) is a one-dimensional rational representation of the elementary abelian group \(T_n\) with character \(\chi_S\); \(\operatorname{wt}(a)\) denotes Hamming weight. No claim is made about a full \(T_n\rtimes S_n\)-irreducible decomposition or the Čech complexes at other scales.

## Proof

**Homological concentration.** Theorem 4.1 of Adams--Shukla--Singh proves \(K_n\simeq\bigvee^{\beta_n}S^2\) for \(n\ge2\), with \(\beta_n\) as above. Thus \(H_0(K_n;\mathbb Q)=\mathbb Q\) with trivial \(T_n\)-action, \(H_2\) has dimension \(\beta_n\), and all other rational homology vanishes.

**Fixed simplices and Lefschetz traces.** Fix a nonzero \(a\in\mathbb F_2^n\). Translation \(x\mapsto x+a\) is a free involution on the vertex set. Any simplex mapped to itself setwise must be a disjoint union of two-element translation orbits \(\{x,x+a\}\). Points of every closed graph neighborhood \(N[v]\) are at Hamming distance at most \(2\). Hence if \(\operatorname{wt}(a)>2\), no nonempty simplex can be fixed setwise, so the alternating trace of the simplicial chain map, \(L(a)\), is zero.

Suppose \(\operatorname{wt}(a)=1\). Within \(N[v]\), the only pair of vertices differing by \(a\) is \(\{v,v+a\}\). Suppose instead \(\operatorname{wt}(a)=2\), supported at \(\{i,j\}\). Within \(N[v]\), the only such pair is \(\{v+e_i,v+e_j\}\). Thus in either case **each** closed neighborhood contains at most one translation orbit, so the only fixed nonempty simplices are edges \(\{x,x+a\}\). Every such edge lies in a neighborhood (a neighbor center for weight \(2\)), and there are \(2^{n-1}\) distinct edges. The involution reverses each oriented edge, giving a trace of \(-1\) on its one-dimensional oriented chain component. Because these are degree-one simplices, each contributes \((-1)^1(-1)=1\) to the simplicial Lefschetz number. Consequently
\[
L(a)=\begin{cases}2^{n-1},&\operatorname{wt}(a)=1\text{ or }2,\\0,&\operatorname{wt}(a)>2.\end{cases}
\]
The Hopf trace formula and homological concentration yield \(L(a)=1+\operatorname{tr}(a\mid H_2(K_n;\mathbb Q))\), proving the asserted trace values. For the identity, the trace is \(\dim H_2=\beta_n\).

**Fourier inversion.** Every irreducible rational representation of \(T_n\) is the rational sign character \(\chi_S\). Character orthogonality gives
\[
m_{n,|S|}=2^{-n}\sum_{a\in T_n}\operatorname{tr}(a\mid H_2)\chi_S(a).
\]
Write \(k=|S|\) and \(d=n-2k\). The weight-one and weight-two character sums are respectively
\[
\sum_{\operatorname{wt}(a)=1}\chi_S(a)=d,\qquad
\sum_{\operatorname{wt}(a)=2}\chi_S(a)=\frac{d^2-n}{2}.
\]
For nonempty \(S\), \(\sum_{a\ne0}\chi_S(a)=-1\). Substitution of the Lefschetz traces gives
\[
m_{n,k}=\frac{n^2-3n+4}{4}+\frac{d}{2}+\frac{d^2-n}{4}=
\binom n2+1-k(n+1-k)\quad(k\ge1).
\]
For \(S=\varnothing\), direct substitution gives \(m_{n,0}=\binom n2\). For \(n=2,3\) the formula is nonnegative by inspection, and for \(n\ge4\) its minimum is at least \(\binom n2+1-\lfloor(n+1)^2/4\rfloor>0\). Orthogonality also gives \(\sum_{k=0}^n\binom nk m_{n,k}=\beta_n\). This proves the complete decomposition and both consequences.

## Verification

The bundled Python 3 standalone script `verify_cech.py` directly constructs faces as subsets of the \(2^n\) closed neighborhoods, enumerates all \(2^n\) translations for \(2\le n\le7\), recomputes signed fixed-face Lefschetz traces, and checks Fourier multiplicities. Over \(\mathbb F_2\), it additionally constructs all simplicial boundaries and computes their ranks for \(2\le n\le5\). It checks dimension identities through \(n=13\). Invoke `python3 verify_cech.py`; `verification_output.txt` records the actual reproduced output.

Representative complete checks give \(n=3\): face vector \((8,24,32,8)\), mod-two Betti vector \((1,0,7,0)\); \(n=4\): face vector \((16,80,160,80,16)\), mod-two Betti vector \((1,0,31,0,0)\). For \(n=4\), multiplicities by character weight \(k=0,1,2,3,4\) are \((6,3,1,1,3)\), summing to \(31\) with binomial weights. These finite computations check the proof in examples; they are not used as an all-dimensional proof.

## Relationship to prior work

Adams, Shukla, and Singh define these intrinsic graph Čech complexes, identify all scale-two facets (Lemma 3.1), and prove the nonequivariant wedge-of-two-spheres theorem (Theorem 4.1). Their result determines only the overall homology dimension, not the translation action or its individual isotypic summands. The present statement adds the all-dimensional equivariant trace and explicit multiplicity decomposition.

Matsushita's later study of closed neighborhood complexes gives natural connections to independence complexes and a graph fundamental group. Its general homotopy equivalences do not state this hypercube translation-character calculation. The literature on Vietoris--Rips complexes of hypercubes, including group-action results, concerns a different simplicial complex: at scale two, these Rips complexes have different homology degrees and cannot imply this Čech representation simply by renaming the space. The original Čech source itself notes the distinction between Čech and Vietoris--Rips constructions.

## Limitations

The theorem covers rational \(T_n\)-representations only, for integer \(n\ge2\) and intrinsic graph Čech scale exactly \(2\). The integer homology wedge type comes from the cited primary theorem; no claim is made that its nonequivariant homotopy equivalence is \(T_n\)-equivariant. The trace proof instead uses the natural simplicial action directly. Computational replay is finite; the all-size conclusion follows from the fixed-simplex argument, Hopf trace formula, published homological concentration, and character orthogonality. Unindexed literature or unpublished results could narrow novelty; independent assessment has not occurred.

## References

1. Henry Adams, Samir Shukla, and Anurag Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871, first posted 2022-12-12, revised 2023-11-20; subsequently *Homology, Homotopy and Applications* 27(1) (2025), 83--105, DOI 10.4310/hha.2025.v27.n1.a6. See Lemma 3.1 and Theorem 4.1. https://arxiv.org/abs/2212.05871.
2. Takahiro Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608, 2025. See Theorems 1.2 and 1.5 and Section 1. https://arxiv.org/abs/2511.12608.
3. Federico Galetto, Jonathan Montaño, and Zoe Wellner, *Homology of Vietoris--Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784, 2026, for the distinct Vietoris--Rips equivariant context. https://arxiv.org/abs/2606.20784.
