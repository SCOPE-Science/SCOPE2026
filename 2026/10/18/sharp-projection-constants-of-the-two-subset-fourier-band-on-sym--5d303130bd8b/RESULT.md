# Sharp projection constants of the two-subset Fourier band on symmetric groups

## Finding

Let \(n\ge4\) be an integer and \(G=S_n\), with the uniform probability measure. Let \(E_n\subset C(G;\mathbb C)\) be the sum of the full matrix-coefficient spaces for the three irreducible representations indexed by \((n)\), \((n-1,1)\), and \((n-2,2)\). Equivalently, \(E_n\) is the span of all matrix coefficients of the permutation representation of \(S_n\) on unordered two-element subsets. Its dimension is
\[
\dim E_n=1+(n-1)^2+\bigl(n(n-3)/2\bigr)^2.
\]

For \(m\ge0\), let \(q_m\) denote the probability that a uniformly random permutation of \(m\) objects has no cycles of length one or two, with \(q_0=1\). The values are determined by the generating function and recurrence
\[
\sum_{m\ge0}q_m z^m=\frac{e^{-z-z^2/2}}{1-z},\qquad
(m+1)q_{m+1}=m q_m+q_{m-2}\quad(m\ge2),
\]
with \(q_1=q_2=0\). Then the absolute complex projection constant of \(E_n\), equal to its relative projection constant in \(C(S_n;\mathbb C)\), is exactly
\[
\boxed{\lambda(E_n)=1+2(n-2)q_n+\bigl(n(n-3)-2\bigr)q_{n-1}+\frac{n(n-5)}2q_{n-2}.}
\]
In particular \(\lambda(E_4)=8/3\) and \(\lambda(E_5)=21/5\). The complete asymptotic expansion through its polynomial part is
\[
\boxed{\lambda(E_n)=1+\tfrac12(3n^2-7n-12)e^{-3/2}+O(n^2 2^{-n}).}
\]
Consequently,
\[
\lim_{n\to\infty}\frac{\lambda(E_n)}{\sqrt{\dim E_n}}=3e^{-3/2}.
\]

Let \(W_n\subset E_n\) denote the single full \((n-2,2)\) matrix-coefficient block. In terms of the known one-block norm \(\lambda(W_n)=n(n-3)(q_{n-1}+q_{n-2}/2)\), the new full-band norm satisfies the strict, unbounded amplification identity
\[
\boxed{\lambda(E_n)-\lambda(W_n)=1+2(n-2)q_n-2q_{n-1}-nq_{n-2}>0\quad(n\ge4),}
\]
and the gap is \(1+(n-6)e^{-3/2}+O(n2^{-n})\).

## Assumptions and scope

All scalars and linear maps are complex. A projection from a Banach space \(Y\) onto its subspace \(X\) means a bounded linear map \(Q:Y\to X\) satisfying \(Qx=x\) for \(x\in X\). The relative projection constant is the infimum of \(\|Q\|\) among such maps. The absolute projection constant \(\lambda(X)\) is the **supremum** of the relative constants over all isometric embeddings of \(X\) into Banach spaces.

For a permutation \(g\), write \(F(g)\) for its number of fixed points and \(T(g)\) for its number of two-cycles. Put \(d=n(n-3)/2\). The orthogonal Fourier projection \(P_n\) onto \(E_n\), normalized by uniform Haar probability, is convolution with the character kernel
\[
K_n(g)=1+(n-1)(F(g)-1)+d\left(\binom{F(g)}2+T(g)-F(g)\right).
\]
This formula fixes all character and probability normalizations. It applies to all integers \(n\ge4\); no infinite-group or general-degree conclusion is asserted.

## Proof

**1. The natural Fourier projection is norm-minimal.** The permutation module on two-element subsets decomposes without multiplicity as the trivial, standard, and \((n-2,2)\) irreducibles. Its permutation character is \(\binom{F(g)}2+T(g)\), since a two-element subset is fixed precisely if both points are fixed or the pair forms a two-cycle. Subtracting the trivial character \(1\) and the standard character \(F-1\) gives \(\chi_{(n-2,2)}=\binom F2+T-F\), of dimension \(d\). Character orthogonality gives the displayed kernel \(K_n\).

The left-right translation action of \(G\times G\) on functions on \(G\) is isometric. Every full matrix-coefficient space is a distinct irreducible bimodule, so averaging any projection onto their sum over \(G\times G\) produces the unique equivariant projection \(P_n\) without increasing its norm. In the sup norm, convolution by a real kernel has norm exactly its normalized \(\ell^1\) mass, as demonstrated by a function matching its signs at one output coordinate. Therefore
\[
\lambda(E_n,C(G;\mathbb C))=\|P_n\|=\frac1{n!}\sum_{g\in G}|K_n(g)|.
\]
This is a special instance of the established equivariant-projection principle [1]. Finally \(C(G;\mathbb C)=\ell_\infty^{n!}\) is injective: coordinatewise Hahn--Banach extensions turn any embedding of \(E_n\) into a contractive map back to this fixed \(\ell_\infty\) realization, so the relative value equals the absolute projection constant.

**2. Exact sign support.** Direct substitution shows that for \(n\ge6\), \(K_n(g)<0\) exactly when \(T(g)=0\) and \(F(g)\in\{0,1,2\}\), with corresponding values \(2-n\), \(1-d\), and \(n-d\). Indeed, with \(T\ge1\) each of the cases \(F=0,1,2\) gives a nonnegative value; for \(F\ge3\), the contribution \(\binom F2-F\) is nonnegative and \(1+(n-1)(F-1)>0\). At \(n=5\) the \(F=2,T=0\) kernel value is zero. At \(n=4\), \(F=2,T=0\) is impossible, since two remaining points must form a two-cycle. Thus the same negative-mass expression below is valid for all \(n\ge4\).

**3. Exact permutation counts.** For \(f,t\ge0\) with \(f+2t\le n\), elementary cycle enumeration gives
\[
\mathbb P\{F=f,T=t\}=\frac{q_{n-f-2t}}{f!\,2^t t!}.
\]
Since \(\mathbb E K_n=1\) by character orthogonality, \(\mathbb E|K_n|=1+2\mathbb E(-K_n)_+\). Using only the three nonpositive strata yields
\[
\mathbb E(-K_n)_+=(n-2)q_n+(d-1)q_{n-1}+\frac{d-n}{2}q_{n-2}.
\]
Substitution of \(d\) proves the exact boxed formula, including the boundary cases \(n=4,5\).

**4. Explicit recurrence, asymptotics, and the non-monotonic block phenomenon.** The exponential formula for permutations with all cycle lengths at least three gives
\[
\sum_{m\ge0}q_m z^m=\exp\!\left(\sum_{j\ge3}\frac{z^j}{j}\right)=\frac{e^{-z-z^2/2}}{1-z}.
\]
Differentiation proves the displayed recurrence. As \(e^{-z-z^2/2}\) is entire, Cauchy's bound at radius two gives \(q_m=e^{-3/2}+O(2^{-m})\). Inserting this in the exact formula gives the quadratic asymptotic, and comparing with \(\dim E_n\sim n^4/4\) gives the normalized limit.

Subtracting the single-block formula yields the stated strict-gap identity. For \(n=4,5\), the exact differences are \(4/3\) and \(1/30\), respectively. The recurrence, with direct bases \(q_4=1/4\), \(q_5=1/5\), \(q_6=2/9\), implies \(1/5\le q_m\le1/4\) for every \(m\ge4\). Hence for \(n\ge6\),
\[
\lambda(E_n)-\lambda(W_n)\ge1+\frac{2(n-2)}5-\frac{n+2}{4}=\frac{3n-6}{20}>0.
\]
The gap asymptotic follows from the same exponential estimate. This ends the proof.

## Verification

The associated self-contained `checker.py` uses Python standard-library exact rational arithmetic. Run `python checker.py`. It enumerates every permutation for \(4\le n\le8\), computes its cycle counts and signed Fourier kernel, checks the sign characterization, and matches the normalized absolute kernel sum to the closed formula. It also checks the recurrence and strict band-versus-block gap in additional finite dimensions. These finite diagnostics corroborate, but do not replace, the proofs for every \(n\ge4\).

## Relationship to prior work

The general averaging and Peter--Weyl projection framework, including the character-kernel norm formula for finite sums of full isotypes of compact groups, is **already established** in [1], especially Corollaries 1.22--1.25. It is *not* a new part of the present finding. A previous exact single-block result [2] determines \(\lambda(W_n)\) by permutations without short cycles, and a related result [3] treats the standard block in doubly transitive actions. Their individual block constants do not determine the \(\ell^1\) norm of the **sum** of three character kernels. The contribution established here is the all-\(n\) formula for that natural complete two-subset band, its exact negative strata, the strict unbounded comparison with the dominant single block, and its sharp normalized limit.

## Limitations

The theorem concerns the full complex two-subset matrix-coefficient band on finite symmetric groups; it does not give individual optimal projections under constraints other than operator norm, nor a classification of every norm-minimizing projection. The underlying general norm-minimization mechanism is prior work. The explicit family formula and comparison have not received independent priority verification; equivalent older symmetric-group calculations could exist, including in literature using Bose--Mesner, association-scheme, or character-algebra language. Finite checker enumeration is not an exhaustive proof over all dimensions.

## References

[1] A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, P. Zadunaisky, *Projection Constants of Polynomial Spaces via Representation Theory*, arXiv:2609.22050v1 (first public September 18, 2026), https://arxiv.org/abs/2609.22050.

[2] *Exact endpoint norms for the \((n-2,2)\) Fourier block of symmetric groups*, publicly indexed mathematical finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-endpoint-norms-for-the-n-2-2-fourier-block-of-symmetric-gr--2557238644ab.

[3] *Derangement density controls the standard Fourier block of every doubly transitive action*, publicly indexed mathematical finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-derangement-density-controls-the-standard-fourier-block-of-every--d168823581e6.
