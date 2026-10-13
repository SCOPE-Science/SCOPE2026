# Nijenhuis operators on Heisenberg Lie algebras: isotropic-image normal forms and exact rank counts

## Finding
Let \(K\) be any field, \(m\geq 1\), and let \((V,\omega)\) be a \(2m\)-dimensional symplectic vector space. Give \(H=V\oplus Kz\) the Heisenberg Lie bracket \([v+tz,w+uz]=\omega(v,w)z\). Every algebraic Nijenhuis operator \(N:H\to H\) has the unique form
\[
N(v+tz)=dv+Sv+\bigl(\ell(v)+dt\bigr)z,
\qquad d\in K,\quad\ell\in V^*,\quad\omega(Sv,Sw)=0\ \text{for all }v,w\in V.
\]
Equivalently, the image of \(S\) is totally isotropic. Conversely, every displayed map is a Nijenhuis operator. Necessarily \(0\leq\operatorname{rank}S\leq m\).

For every finite field \(K=\mathbb F_q\), including even characteristic, the number of such operators with \(\operatorname{rank}S=r\) is exactly
\[
C_{m,r}(q)=q^{2m+1}{m\brack r}_q
\left(\prod_{i=0}^{r-1}(q^{m-i}+1)\right)
\left(\prod_{i=0}^{r-1}(q^{2m}-q^i)\right),\qquad 0\leq r\leq m.
\]
Empty products equal one and Gaussian coefficients have their usual subspace-count meaning. Hence the total number is \(\sum_{r=0}^m C_{m,r}(q)\). In the smallest case it simplifies to \(q^6+q^5-q^4\) for \(m=1\); when \(m=2,q=2\), the total is \(2^5(1+225+3150)=108032\).

The rank-\(r\) locus is a smooth, geometrically irreducible locally closed variety of dimension
\[
r(2m-r)-\binom r2+2mr+2m+1.
\]
The underlying reduced variety of all Nijenhuis operators is geometrically irreducible of dimension \((5m^2+5m+2)/2\).

## Assumptions and scope
An algebraic Nijenhuis operator on a Lie algebra is a \(K\)-linear map satisfying, for all \(x,y\),
\[
[Nx,Ny]=N\bigl([Nx,y]+[x,Ny]-N[x,y]\bigr).
\]
The alternating nondegenerate form \(\omega\) is assumed fixed, and \(H\) is its one-dimensional central extension. The result concerns *all labeled linear maps* \(H\to H\), not equivalence classes modulo automorphisms. The theorem includes characteristic two: an alternating bilinear form is not the same as a symmetric form in that characteristic. For the finite-field count, \(q\) can be any prime power and \(r\) an integer from zero through \(m\).

## Proof
**Step 1 (the center cannot acquire a noncentral image).** Write any linear operator in block form as
\[
N(v)=Av+\ell(v)z,\qquad N(z)=b+dz,
\]
where \(A\in\operatorname{End}(V)\), \(\ell\in V^*\), \(b\in V\) and \(d\in K\). The Nijenhuis identity for the pair \((v,z)\) reads
\[
\omega(Av,b)z=\omega(v,b)(b+dz).
\]
Comparing the \(V\)-components gives \(\omega(v,b)b=0\) for every \(v\). If \(b\ne0\), nondegeneracy of \(\omega\) produces \(v\) with \(\omega(v,b)\ne0\), a contradiction. Hence \(b=0\).

**Step 2 (the exact torsion equation).** With \(b=0\), evaluation on arbitrary \(v,w\in V\) gives
\[
\omega(Av,Aw)=d\bigl(\omega(Av,w)+\omega(v,Aw)-d\omega(v,w)\bigr).
\]
Put \(S=A-d\operatorname{id}_V\). Bilinearity makes the difference between the left and right sides exactly \(\omega(Sv,Sw)\). Therefore the Nijenhuis identity holds if and only if \(\omega(Sv,Sw)=0\) for all \(v,w\). No condition is imposed on \(\ell\). Pairs involving \(z\) automatically satisfy the identity once \(b=0\). The decomposition into \(d,S,\ell\) is unique. A totally isotropic subspace of a nondegenerate symplectic \(2m\)-space has dimension at most \(m\).

**Step 3 (finite-field isotropic image counting).** Fix \(r\). The number \(I_m(r)\) of totally isotropic \(r\)-dimensional subspaces of \(V\) is
\[
I_m(r)=\frac{\prod_{i=0}^{r-1}(q^{2m-i}-q^i)}{\prod_{i=0}^{r-1}(q^r-q^i)}
={m\brack r}_q\prod_{i=0}^{r-1}(q^{m-i}+1).
\]
Indeed, once \(i\) independent mutually orthogonal vectors have been chosen, the next lies in their symplectic orthogonal (of size \(q^{2m-i}\)) but outside their span (of size \(q^i\)); division by the number of ordered bases of an \(r\)-space counts image subspaces. For a fixed \(r\)-dimensional image \(W\), the number of surjective maps \(S:V\twoheadrightarrow W\) is \(\prod_{i=0}^{r-1}(q^{2m}-q^i)\). The independent choices of \(d\) and \(\ell\) contribute \(q\) and \(q^{2m}\), respectively. Multiplying proves the exact formula. Distinct image subspaces do not double-count \(S\), as \(\operatorname{im}S\) is uniquely determined.

**Step 4 (geometry).** The isotropic Grassmannian of \(r\)-planes in a symplectic \(2m\)-space is smooth and geometrically irreducible of dimension \(r(2m-r)-\binom r2\). The rank-\(r\) operator locus is the bundle of surjections \(V\twoheadrightarrow W\) over that Grassmannian, together with affine factors \(K\) and \(V^*\). Its dimension and smooth irreducibility follow. Every isotropic image \(\operatorname{im}S\) lies in a Lagrangian subspace \(W\), so the entire variety is the image of the total space of the rank-\(2m^2\) vector bundle \(\operatorname{Hom}(V,W)\) over the Lagrangian Grassmannian, times \(K\times V^*\). This image is the full Nijenhuis variety and is irreducible, also after algebraic closure. The rank-\(m\) locus is dense and has dimension \(m(m+1)/2+2m^2+2m+1=(5m^2+5m+2)/2\). The irreducibility statement refers to the underlying reduced variety; no assertion about a particular presentation being scheme-theoretically reduced is needed.

## Verification
Run `python3 verify.py` from the directory containing the bundled standalone script. It prints `VERIFY_OK` on success. The script directly evaluates the Nijenhuis torsion on all basis pairs of every one of the \(q^9\) linear operators for \(m=1\) over \(\mathbb F_2\) and \(\mathbb F_3\), obtaining respectively \(80\) and \(891\) solutions and checking that the normal form identifies exactly those. It exhaustively enumerates the admissible \(S\)-matrices for \(m=1\) over \(q=2,3,5\) and for \(m=2\) over \(q=2\), matching rank counts \((1,9)\), \((1,32)\), \((1,144)\), and \((1,225,3150)\). Additional deterministic random matrix checks compare the direct torsion equation with the normal form for \((m,q)=(1,5),(2,2),(2,3),(3,2)\). These computations check examples only; Steps 1–4 prove the arbitrary-field and all-prime-power statements.

## Relationship to prior work
Mondal and Saha, *Nijenhuis operators on Leibniz algebras* (arXiv:2306.06428v1, 2023), provide the general Nijenhuis framework, representation, cohomology and deformation theory. Their examples do not give a classification for nonabelian Heisenberg Lie algebras or its complete rank distribution. Zhikhareva, *Three-dimensional Lie algebras admitting regular semisimple algebraic Nijenhuis operators* (arXiv:2410.10536v1, 2024), studies the disjoint regular semisimple regime and rules it out on nonabelian nilpotent three-dimensional Lie algebras; elementary central Nijenhuis operators are already familiar. Ma and Zhao, *Classification of three-dimensional Nijenhuis Leibniz algebras* (arXiv:2507.12692v1, 2025), give explicit matrices for thirteen real Leibniz-algebra types, not a uniform symplectic-rank count across all Heisenberg dimensions and finite characteristics. Gao and collaborators (arXiv:2308.12121v1; subsequently revised) treat pre-Lie and associative Nijenhuis operators, not the present Lie-operator census. The known definitions, trivial scalar examples and all overlapping special cases are not claimed as new. The contribution asserted here is the general structural equivalence, complete symplectic rank stratification, and finite-field enumeration.

## Limitations
No classification modulo the Heisenberg automorphism group is claimed. The geometric statement is about reduced algebraic varieties, not a full nonreduced scheme structure. The finite checks cannot prove infinitely many cases independently of the mathematical proof. Search-based comparisons cannot rule out every alternative terminology or uncatalogued prior treatment; especially, an exact earlier rank enumeration may exist outside the inspected sources. No independent external audit has been conducted.

## References
1. Bibhash Mondal and Ripan Saha, *Nijenhuis operators on Leibniz algebras*, arXiv:2306.06428v1 (first public submission 2023-06-10), https://arxiv.org/abs/2306.06428.
2. Ekaterina S. Zhikhareva, *Three-dimensional Lie algebras admitting regular semisimple algebraic Nijenhuis operators*, arXiv:2410.10536v1 (2024-10-14), https://arxiv.org/abs/2410.10536.
3. Tianshui Ma and Chan Zhao, *Classification of three-dimensional Nijenhuis Leibniz algebras*, arXiv:2507.12692v1 (2025-07-16), https://arxiv.org/abs/2507.12692.
4. Xiang Gao and collaborators, *Nijenhuis operators on 2D pre-Lie algebras and 3D associative algebras*, arXiv:2308.12121 (first public 2023-08-23; later revisions), https://arxiv.org/abs/2308.12121.
