# Socle product-matrix spectra detect Witt type in four-dimensional finite local Gorenstein algebras

## Finding

Let \(q\ge2\) be a prime power, and let \(R\) be a commutative unital, four-dimensional \(\mathbb F_q\)-algebra, local with maximal ideal \(\mathfrak m\), such that
\[
\mathfrak m^3=0,\qquad \dim_{\mathbb F_q}(\mathfrak m/\mathfrak m^2)=2,\qquad \dim_{\mathbb F_q}\mathfrak m^2=1,\qquad \operatorname{Soc}(R)=\mathfrak m^2.
\]
(The last condition is the Artinian Gorenstein condition.) For a fixed nonzero \(u\in\mathfrak m^2\), define the real symmetric matrix indexed by all elements of \(R\):
\[
 A_u(R)_{a,b}=\begin{cases}1,&ab=u,\\0,&ab\ne u.\end{cases}
\]
Multiplication on \(\mathfrak m/\mathfrak m^2\) induces a nondegenerate symmetric bilinear form \(B\) with values in \(\mathfrak m^2\cong\mathbb F_q\). Let \(t\) denote its number of isotropic projective lines:
\[
 t=\#\{\ell\in\mathbb P(\mathfrak m/\mathfrak m^2):B(v,v)=0\text{ for }0\ne v\in\ell\}.
\]
Then \(t\in\{0,2\}\) for odd \(q\) and \(t\in\{1,q+1\}\) for even \(q\). Put \(K=(q^2+q-4)/2\). **The full characteristic polynomial is**
\[
\boxed{\det(XI-A_u(R))=X^{q^4-q^2-2q+3}(X-q^2)(X-q)^{(q+1-t)/2}(X+q)^{(q-1+t)/2}(X^2-q^3)^K.}
\]
The spectrum is independent of the chosen nonzero socle target. Its signed \(\pm q\) multiplicities recover \(t\), and hence distinguish the split/anisotropic Witt types in odd characteristic and the alternating/nonalternating types in characteristic two. Its rank is \(q^2+2q-3\).

## Assumptions and scope

All vector-space dimensions and bilinear forms are over \(\mathbb F_q\); all matrix eigenvalues and characteristic polynomials are over \(\mathbb R\). The ring is assumed to be an \(\mathbb F_q\)-algebra (equicharacteristic and with a specified coefficient field), not an arbitrary local ring with residue field of order \(q\). The maximal ideal has Hilbert function \((1,2,1)\) and nondegenerate socle pairing. The target is required to be nonzero and in \(\mathfrak m^2\); claims about targets outside this set are not made.

By choosing a coefficient-field complement and a two-dimensional lift \(V\) of \(\mathfrak m/\mathfrak m^2\), and a socle generator \(z\), one has \(R=\mathbb F_q\oplus V\oplus\mathbb F_q z\) with multiplication
\[
(a,v,bz)(a',v',b'z)=(aa',av'+a'v,(ab'+a'b+B(v,v'))z).
\]
The bilinear form \(B\) is symmetric by commutativity; its radical is zero because \(\operatorname{Soc}(R)=\mathfrak m^2\). Conversely this formula defines every ring in the stated class. Scaling \(z\) changes \(B\) by an overall nonzero scalar but not \(t\).

## Proof

**1. Characteristic blocks.** Fix \(u=cz\) with \(c\ne0\). The vertex sets of \(A_u(R)\) are the units (\((q-1)q^3\) elements), the nonzero socle (\(q-1\) elements), the zero element, and the elements of \(\mathfrak m\setminus\mathfrak m^2\) (\(q(q^2-1)\) elements). A unit with nonzero residue \(a\) multiplies to \(u\) with exactly one socle element, \((c/a)z\), and with no other element. For each \(a\in\mathbb F_q^\times\), the \(q^3\) units of residue \(a\) and the single socle element \((c/a)z\) therefore induce an isolated star \(K_{1,q^3}\), with nonzero eigenvalues \(\pm q^{3/2}\), once each. The zero element is isolated.

On \(\mathfrak m\setminus\mathfrak m^2\), vertices can be indexed by \((v,b)\) with \(0\ne v\in V\) and \(b\in\mathbb F_q\). Two such elements multiply to \(u\) exactly when \(B(v,w)=c\), independently of their last coordinates. Thus the remaining block is \(C\otimes J_q\), where \(J_q\) is the all-ones \(q\)-by-\(q\) real matrix and
\[
 C_{v,w}=\mathbf1_{B(v,w)=c},\qquad v,w\in V\setminus\{0\}.
\]
Its nonzero spectrum is \(q\) times the spectrum of \(C\). It remains to diagonalize \(C\).

**2. Counting two-step walks.** For nonzero \(v,w\), the entry \((C^2)_{v,w}\) counts \(y\ne0\) with \(B(v,y)=B(w,y)=c\). Nondegeneracy gives
\[
(C^2)_{v,w}=\begin{cases}q,&v=w,\\0,&v\ne w\text{ and }\langle v\rangle=\langle w\rangle,\\1,&\langle v\rangle\ne\langle w\rangle.\end{cases}
\]
Indeed proportional unequal equations are incompatible because \(c\ne0\); independent equations have a unique, necessarily nonzero solution. Let \(\mathcal L\) be the \(q+1\) projective lines in \(V\), and let \(H\) be the space of functions on \(V\setminus0\) constant on each line. Its orthogonal complement \(U\) consists of functions whose sum along each line is zero, of dimension \((q+1)(q-2)\). The preceding formula shows \(C^2=qI\) on \(U\).

**3. The line-constant spectrum.** Since \(B\) is symmetric and nondegenerate, \(\ell\mapsto\ell^\perp\) is an involution on \(\mathcal L\), fixing precisely the \(t\) isotropic lines. For \(f\in H\) and \(v\in\ell\setminus0\), exactly one nonzero \(w\) in each line different from \(\ell^\perp\) satisfies \(B(v,w)=c\). Hence, on \(H\),
\[
 C=\mathbf1\mathbf1^\top-P,
\]
where \(P\) is the permutation matrix of the perpendicular-line involution and \(\mathbf1\mathbf1^\top\) is the \((q+1)\)-by-\((q+1)\) all-ones matrix. The constant vector has eigenvalue \(q\). The involution has \(t\) fixed points and \((q+1-t)/2\) two-cycles. Thus on the sum-zero complement in \(H\), the \(+1\) eigenvalue of \(C\) has multiplicity \((q+1-t)/2\) and the \(-1\) eigenvalue has multiplicity \((q-1+t)/2\).

**4. Signs on the remaining block.** Since \(C\) is real symmetric and \(C^2=qI\) on \(U\), all eigenvalues there are \(+\sqrt q\) or \(-\sqrt q\). They occur equally often. To see this, note that \(\operatorname{tr}C\) counts \(0\ne v\in V\) with \(B(v,v)=c\). This number is \(q+1-t\): for odd \(q\), a split binary form has \(q-1\) representations of each nonzero value and two isotropic lines, while an anisotropic binary form has \(q+1\) representations and no isotropic line; for even \(q\), a nonalternating form has one isotropic line and \(q\) representations, while an alternating form has \(q+1\) isotropic lines and no representations. The trace of \(C\) on \(H\) is already \(q+1-t\), by step 3. Thus \(\operatorname{tr}(C|_U)=0\), and the two signs each have multiplicity \((q+1)(q-2)/2\).

**5. Characteristic polynomial and rank.** Scale the nonzero eigenvalues of \(C\) by \(q\), add one pair \(\pm q^{3/2}\) for each of the \(q-1\) stars, and pad with zeros to reach the total dimension \(q^4\). The multiplicities of \(\pm q^{3/2}\) are each \((q-1)+(q+1)(q-2)/2=K\), and the positive and negative \(q\) multiplicities are those in step 3. Exactly \((q^2-1)+2(q-1)=q^2+2q-3\) eigenvalues are nonzero, giving the displayed zero multiplicity and the asserted polynomial. All eigenvalues are separated for \(q\ge2\), so their multiplicities determine \(t\). This proves the theorem.

## Verification

A standalone script `verify.py` independently forms the finite-field bilinear incidence matrices and, for \(q=2,3,4\), the complete product matrices, without using the block decomposition in the full-matrix construction. It checks multiplicities for both bilinear-form types in each field. It additionally checks the incidence spectra for two form types over \(\mathbb F_5\). The script reports `OK` for all eight cases. Its extension-field case uses the polynomial \(X^2+X+1\) for \(\mathbb F_4\). The numerical diagonalization is corroborative only; steps 1–5 constitute the proof for all prime powers.

For \(q=2\), the alternating case has \(t=3\) and spectrum encoded by \(X^{11}(X-4)(X+2)^2(X^2-8)\); the nonalternating case has \(t=1\) and spectrum encoded by \(X^{11}(X-4)(X-2)(X+2)(X^2-8)\). For \(q=3\), the split and anisotropic cases respectively have \(t=2\) and \(t=0\); the \(+3\) and \(-3\) multiplicities interchange.

## Relationship to prior work

David Dolžan, *Eigenvalues of the product matrices of finite commutative rings*, arXiv:2601.19301 (first posted 2026-01-27; journal version in *Linear and Multilinear Algebra*, 2026), introduces and studies \(A_u(R)\). Its publicly indexed introduction describes local-ring results for unit targets and radical nilpotency at the maximal/minimal extremes. The local rings here have nilpotency index three between those extremes and a nonzero socle target. The method here is a finite-field bilinear-incidence decomposition, and the sign asymmetry detects the Witt type. The arXiv preprint was inspected through its complete 12-page text and targeted page images: its Theorem 3.1 covers unit targets, Theorems 4.1, 4.4, and 4.7 assume maximal radical nilpotency (for order \(q^4\), \(\mathfrak m^3\ne0\)), and Theorem 5.1 assumes \(\mathfrak m^2=0\). None implies the intermediate \(\mathfrak m^3=0\ne\mathfrak m^2\) case considered here. Historical priority remains qualified only for potentially equivalent results elsewhere in the literature.

Finite-field binary quadratic-form classification and elementary spectral decomposition of incidence matrices are standard ingredients, not claimed as new. The structural novelty claimed is the ring-theoretic characteristic polynomial for this intermediate-nilpotence Gorenstein class and its Witt-type recovery.

## Limitations

The theorem makes no assertion for degenerate socle pairings, non-split coefficient fields, higher embedding dimension, zero targets, or targets outside the socle. It gives real adjacency-matrix multiplicities (loops permitted), not the loopless graph spectrum, and is not an independent mathematical validation. The motivating preprint was inspected; an exhaustive comparison with all possible historical variants has not been completed.

## References

1. D. Dolžan, *Eigenvalues of the product matrices of finite commutative rings*, arXiv:2601.19301, first submitted 2026-01-27; *Linear and Multilinear Algebra* **74** (2026), 449–461, DOI: 10.1080/03081087.2026.2625381.
2. A. E. Brouwer and W. H. Haemers, *Spectra of Graphs*, Springer, 2012 (general matrix and graph-spectral background).
3. T. Y. Lam, *Introduction to Quadratic Forms over Fields*, American Mathematical Society, 2005 (classification of binary forms, standard background).
