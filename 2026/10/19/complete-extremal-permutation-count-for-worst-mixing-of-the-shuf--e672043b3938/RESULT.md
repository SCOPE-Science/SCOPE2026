# Complete extremal-permutation count for worst mixing of the shuffled doubling map

## Finding

For every odd integer \(N\ge 3\), partition \([0,1)\) into the \(N\) equal half-open intervals \(I_j=[j/N,(j+1)/N)\), indexed by \(j\in\mathbb Z/N\mathbb Z\). Let \(D(x)=2x\pmod 1\), and for each permutation \(\sigma\) of the interval indices let \(S_\sigma\) translate \(I_j\) onto \(I_{\sigma(j)}\) without reversal. Denote by \(\tau(\sigma)\) the spectral mixing rate of \(S_\sigma\circ D\) on bounded-variation observables: the largest modulus of the transfer-operator spectrum other than the leading eigenvalue \(1\).

The known sharp upper bound is \(\tau(\sigma)\le\cos(\pi/N)\). We classify **all** permutations attaining this bound and count them exactly:

\[
\boxed{\#\{\sigma:\tau(\sigma)=\cos(\pi/N)\}=N\,2^{(N-1)/2}.}
\]

For a constructive classification, set \(h=(N-1)/2\) and associate to each original permutation \(\sigma\) its effective permutation

\[
\rho(i)\equiv 2\sigma(i)-h\pmod N.
\]

For each \(a\in\mathbb Z/N\mathbb Z\), let \(H_a\) be the group of permutations obtained by **independently** swapping or not swapping each pair \(\{i,a-i\}\), with the unique solution of \(2i=a\) fixed. (There are \(h\) pairs and hence \(|H_a|=2^h\).) Then equality holds if and only if \(\rho\) is either a cyclic rotation \(i\mapsto i+c\) or an element of one of the \(H_a\). The intersection of distinct \(H_a\) is the identity, and no nonidentity rotation lies in any \(H_a\).

Moreover, the nonleading eigenvalues lying on the extremal circle of radius \(\cos(\pi/N)\) are restricted to

\[
-\cos(\pi/N)e^{2\pi\mathrm{i}c/N}\quad(c\in\mathbb Z/N\mathbb Z),\qquad
+\cos(\pi/N).
\]

Every displayed location occurs, and no other point on that circle occurs. Thus the doubling-map case of the outer-circle assertion in Conjecture 2.4.1 of Byott--Holland--Zhang is settled. The new content is the equality-case rigidity and exact enumeration; the magnitude of the sharp upper bound and examples attaining it were already known.

For uniform random \(\sigma\), the exact proportion of worst-mixing shuffles is \(N2^{(N-1)/2}/N!\); for \(N=3,5,7\) the counts are \(6,20,56\), respectively.

## Assumptions and scope

The result concerns only odd integers \(N\ge3\), the standard orientation-preserving doubling map, equal-length interval-exchange permutations, and the bounded-variation transfer spectrum. It does not assert an optimizer count for even \(N\), higher expanding slopes, tent-map variants, or arbitrary interval exchanges. The subleading matrix spectrum and transfer spectral correspondence use the published Markov-partition reduction of Byott--Holland--Zhang, recalled explicitly below.

Throughout, a permutation matrix for a bijection \(p\) has entries \(P(p)_{i,j}=1\) exactly when \(j=p(i)\), so \((P(p)v)_i=v_{p(i)}\). All residue arithmetic is modulo \(N\).

## Proof

**Step 1: reducing the dynamical spectrum to a symmetric circulant.** The standard \(N\)-state matrix for the shuffled expanding map has entries

\[
A_{i,j}=\mathbf1_{\{j=2i\text{ or }j=2i+1\}}.
\]

For a shuffle \(\sigma\), its normalized matrix is \(M_\sigma=\tfrac12 A P(\sigma)\). In the full Markov partition of \(2N\) cells, the transfer matrix is \(\tfrac12 BQ(\sigma)\) in the notation of Byott--Holland--Zhang, Lemma 4.2.1; its **nonzero** eigenvalues, with algebraic multiplicities, agree with those of \(M_\sigma\). The essential spectral radius on \(BV\) is \(1/2\), and for odd \(N\) every shuffle is mixing (their Theorems 1 and 2). Consequently the actual mixing rate is

\[
\tau(\sigma)=\max\left\{\frac12,\ \max_{\lambda\in\operatorname{spec}(M_\sigma)\setminus\{1\}}|\lambda|\right\}.
\]

Write \(h=(N-1)/2\) and let \(C\) be the \(N\)-by-\(N\) symmetric circulant matrix

\[
C_{i,j}=\mathbf1_{\{j=i+h\text{ or }j=i-h\}}.
\]

Let \(r(i)=2i-h\) and \(R=P(r)\). Because \(2h\equiv-1\pmod N\), \(A=RC\). Hence

\[
R^{-1}M_\sigma R=\frac12 CP(\sigma)R=\frac12 CP(\rho),\quad
\rho(i)=r(\sigma(i))=2\sigma(i)-h.
\]

The correspondence \(\sigma\leftrightarrow\rho\) is bijective because \(r\) is a permutation when \(N\) is odd. It therefore suffices to classify extremal \(P=P(\rho)\) for \(T=CP/2\).

**Step 2: exact top Fourier singular space.** Let \(\omega=e^{2\pi\mathrm{i}/N}\) and \(f_k=(\omega^{ki})_{i=0}^{N-1}\). The centered circulant \(B=C/2\) satisfies

\[
B f_k=\cos(2\pi hk/N)f_k=(-1)^k\cos(\pi k/N)f_k.
\]

The constant vector \(f_0\) has eigenvalue \(1\). On its orthogonal complement the exact operator norm is \(t=\cos(\pi/N)\), attained **only** on the complex two-dimensional space

\[
E=\operatorname{span}_{\mathbb C}\{f_1,f_{N-1}\},\qquad B|_E=-tI.
\]

This uniqueness follows from \(|\cos(\pi k/N)|<\cos(\pi/N)\) for \(2\le k\le N-2\), with an empty inequality range for \(N=3\). Since \(P\) is unitary and fixes the constant vector, every nonleading eigenvalue of \(BP\) has modulus at most \(t\).

Crucially, an eigenvalue \(\lambda\) of \(BP\) has \(|\lambda|=t\) **if and only if** \(P\) has a nonzero eigenvector \(v\in E\). Indeed, \(BPv=\lambda v\) at equality forces \(Pv\in E\) by equality in the Fourier norm bound. As \(B=-tI\) on \(E\), this yields \(Pv=-\lambda v/t\) and \(v\in E\). Conversely, if \(Pv=\eta v\) for \(v\in E\), then \(BPv=-t\eta v\). Thus the problem reduces exactly to the permutation eigenvectors lying in the first Fourier harmonic.

**Step 3: nonreal boundary eigenvalues force global dihedral symmetry.** If \(Pv=\eta v\) for \(v\in E\), with \(\eta\notin\{1,-1\}\), then \(v\) and its complex conjugate are independent and span \(E\), because \(P\) is real and their eigenvalues differ. Hence \(P E=E\). Equivalently, permuting the rows of the real matrix with columns

\[
\left(\cos(2\pi i/N),\ \sin(2\pi i/N)\right)
\]

maps these columns into their two-dimensional real span. Orthogonality of \(P\), together with the matrix's Gram matrix \((N/2)I_2\), forces the induced transformation of the regular \(N\)-gon to be orthogonal. Every such symmetry is dihedral: \(\rho(i)=i+c\) or \(\rho(i)=a-i\). Reflections have only real eigenvalues on \(E\). Thus all nonreal extremal eigenvalues come from rotations and equal \(-t e^{\pm2\pi\mathrm{i}c/N}\), and all nonidentity rotations attain \(t\).

**Step 4: fixed cosine modes and independent reflection-pair swaps.** Since \(P\) is real, for eigenvalue \(\eta=1\) in \(E\) we may take a real vector of the form \(v_i=\cos(2\pi i/N-\phi)\). Suppose \(\rho\ne\mathrm{id}\) and \(Pv=v\). Then some distinct \(i,j\) satisfy \(v_i=v_j\), which is equivalent to

\[
\phi\equiv\pi (i+j)/N\pmod\pi.
\]

For a given such phase, write \(a=i+j\). Its equal-value classes consist precisely of the \(h\) pairs \(\{k,a-k\}\) and the unique singleton satisfying \(2k=a\); there are no larger classes, since each equation \(\cos\theta=c\) has at most two solutions modulo a full turn. Therefore \(Pv=v\) exactly when \(\rho\in H_a\), with all pair swaps independent. Every \(P\in H_a\) fixes the corresponding cosine vector and gives the boundary eigenvalue \(\lambda=-t\).

**Step 5: sign-reversing cosine modes introduce no extra permutations.** Suppose \(Pv=-v\) for a nonzero real \(v\in E\) written in the same cosine form. The multiset of its coordinates must be invariant under negation. Since \(N\) is odd, its odd \(N\)-th power sum therefore vanishes. Root-of-unity filtering in the binomial expansion gives the exact identity

\[
\sum_{j=0}^{N-1}\cos^N(2\pi j/N-\phi)
=\frac{N}{2^{N-1}}\cos(N\phi).
\]

Hence \(\cos(N\phi)=0\), or \(\phi\equiv(2k+1)\pi/(2N)\pmod\pi\). At such a phase all sampled values are distinct: an equality between distinct coordinates would instead force \(\phi\equiv\pi a/N\pmod\pi\), impossible here. There is therefore a **unique** permutation taking \(v\) to \(-v\). It is a reflection \(\rho(i)=a-i\), where \(a\equiv N/2+N\phi/\pi\pmod N\), which is an integer because \(N\) is odd. This reflection belongs to \(H_a\). It produces \(\lambda=+t\), but yields no additional extremizers.

**Step 6: exact count and outer-circle locations.** Each \(H_a\) has \(2^h\) elements. If \(a\ne b\), a permutation in \(H_a\cap H_b\) would fix two linearly independent real cosine vectors spanning \(E\). It would then fix every vertex of the regular \(N\)-gon and must be the identity. Therefore

\[
\left|\bigcup_{a\in\mathbb Z/N\mathbb Z}H_a\right|
=1+N(2^h-1).
\]

Any nonidentity rotation moves every vertex and hence does not lie in the union, since every element of \(H_a\) fixes the singleton \(2i=a\). Adding the \(N-1\) nonidentity rotations gives

\[
1+N(2^h-1)+(N-1)=N2^h.
\]

The rotation and reflection eigenvalues computed above also prove that the only possible eigenvalues on the outer circle are \(-t e^{2\pi\mathrm{i}c/N}\) and \(+t\), and that they all occur. Finally, \(t>1/2\) for \(N\ge5\), so maximizing the matrix subleading modulus is equivalent to maximizing the transfer mixing rate. For \(N=3\), \(t=1/2\) and all \(3!=6=3\cdot2^1\) shuffles attain it, precisely as the same classification predicts. This completes the proof.

## Verification

Run `python verify.py` with Python 3 and NumPy installed. The checker constructs the exact transition matrices for each permutation at \(N=3,5,7\), checks their conjugacy, computes every subleading eigenvalue numerically, and checks equality against the explicit rotation/reflection-pair classification and the counts \(6,20,56\). It also verifies independent combinatorial classification counts and randomly sampled examples at \(N=9\). A successful run prints `VERIFY_OK`.

The finite numerical checks are corroborative: the theorem for all odd \(N\) follows from Steps 1--6, not the finite enumeration.

## Relationship to prior work

Byott, Holland and Zhang (arXiv:1203.5145, first publicly posted 22 March 2012) proved that for coprime slope and cell count the maximal transfer mixing rate equals \(\sin(m\pi/N)/(m\sin(\pi/N))\), and exhibited permutations attaining the bound. In the doubling case this is \(\cos(\pi/N)\). Their Section 4 derives the finite Markov spectral correspondence and the circulant singular-value inequality. Their Conjecture 2.4.1 concerns the geometric location of eigenvalues on the extremal circle. The present theorem supplies the **complete equality classification**, the closed-form number of extremizing shuffles, and a proof of that conjecture's boundary assertion when \(m=2\) and \(N\) is odd. It does not prove the conjecture for other slopes.

Byott, Lin and Zhang (arXiv:1405.0481, first posted 2 May 2014), studying maps with varying branch orientation, recover and extend the worst-rate value for stretch-and-fold maps; their inspected results do not enumerate the maximizing shuffles. The counting result here is not implied by knowing only that an upper bound is sharp: its proof needs the equality cases in the Fourier singular-value argument, including many non-dihedral partial pair swaps.

## Limitations

The reduction to the transfer operator invokes the established Markov-partition spectral correspondence and essential-radius result from the cited first paper. All new equality and counting arguments are proved here. Independent external validation has not been performed. The classification is stated for odd \(N\), and it does not describe the entire interior isolated spectrum or arbitrary smooth observables outside the indicated bounded-variation setting. Literature searches do not prove absolute historical priority; an unindexed antecedent specializing the exact equality cases is possible.

## References

1. N. P. Byott, M. Holland and Y. Zhang, *On the mixing properties of piecewise expanding maps under composition with permutations*, arXiv:1203.5145 (first posted 2012-03-22), Discrete and Continuous Dynamical Systems 33 (2013), 3365--3390, DOI: 10.3934/dcds.2013.33.3365. Especially Theorems 1--2, Lemmas 4.2.1--4.2.3, Conjecture 2.4.1.
2. N. P. Byott, C. Lin and Y. Zhang, *On the mixing properties of piecewise expanding maps under composition with permutations, II: Maps of non-constant orientation*, arXiv:1405.0481 (first posted 2014-05-02). Especially Theorem 4 and its proof.
