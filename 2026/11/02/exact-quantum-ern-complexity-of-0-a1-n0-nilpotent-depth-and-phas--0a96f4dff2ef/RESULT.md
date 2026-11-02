# Exact quantum Černý complexity of \(0^a1^n0\): nilpotent depth and phase counting

## Finding

Let \(\operatorname{qc}(w)\) be the minimum Hilbert-space dimension in which a pair of quantum channels has \(w\) as its **unique shortest** word acting constantly on the states reachable from one initial density matrix, in the mixed-target sense of [1]. For all integers \(a,n\geq1\),

\[
\boxed{\operatorname{qc}(0^a1^n0)=\left\lceil\sqrt{a+2}\right\rceil.}
\]

Thus varying the middle run length \(n\) has no effect on the optimal dimension. In particular, \(\operatorname{qc}(0^a1^n0)=2\) exactly when \(a\in\{1,2\}\); for \(a\geq3\) a qubit is impossible. The previously known case \(a=1\) is included for context, not claimed as new. The additional structural statement is that the least dimension of real matrices whose unique shortest zero product is \(0^a1^n0\) equals \(a+1\).

## Assumptions and scope

The alphabet is \(\{0,1\}\), and words act left to right: for real-linear maps \(X,Y\) attached to letters \(0,1\), the word \(0^a1^n0\) acts as \(XY^nX^a\). A word is synchronizing when the corresponding channel is constant on the entire reachable set of a fixed initial density matrix. The target may be mixed; no claim about the pure-target invariant is made. Parameters \(a,n\) are arbitrary positive integers, and dimension refers to the complex Hilbert-space dimension, not the real dimension of the density-operator space.

For any instance, put \(R=\{A_u(\rho_0):u\in\{0,1\}^*\}\) and \(V=\operatorname{span}_{\mathbb R}(R-R)\). On traceless Hermitian matrices, the channels induce real-linear maps \(L_0,L_1\), preserving \(V\); a word synchronizes exactly when its linear part vanishes on \(V\). Here \(\dim_{\mathbb R}V\leq d^2-1\). This elementary linearization is also Proposition 2.1 of [1].

## Proof

**1. Lower bound.** Suppose \(0^a1^n0\) is a unique shortest synchronizing word in dimension \(d\). Write \(X=L_0|_V\) and \(Y=L_1|_V\). We have

\[XY^nX^a=0.\]

Because \(0^a\) and \(0^{a-1}1^n0\) are strictly shorter than the proposed shortest word, respectively,

\[X^a\neq0,\qquad XY^nX^{a-1}\neq0.\]

Consequently \(\operatorname{im}X^a\) is a **proper** subspace of \(\operatorname{im}X^{a-1}\). For a linear map on a finite-dimensional space, once \(\operatorname{rank}X^j=\operatorname{rank}X^{j+1}\), the images coincide and the subsequent ranks remain equal. Thus a strict rank drop at exponent \(a\) forces a strict drop at every exponent \(1,\ldots,a\). Moreover \(\operatorname{rank}X^a\geq1\). It follows that

\[
\dim_{\mathbb R}V\geq a+1.
\]

Hence \(d^2-1\geq a+1\) and \(d\geq\lceil\sqrt{a+2}\rceil\). Notice that the argument works for **all** quantum channels, without assuming a particular Kraus representation or unitality.

**2. A sharp real-matrix construction.** Let \(U=\mathbb R^{a+1}\) with ordered basis \(e_0,e_1,\ldots,e_a\), and put \(\theta=\pi/(2n)\). Define

\[
Xe_0=e_0,\quad Xe_1=0,\quad Xe_j=e_{j-1}\ (2\leq j\leq a),
\]

\[
Ye_0=\cos\theta\,e_0+\sin\theta\,e_1,\quad
Ye_1=-\sin\theta\,e_0+\cos\theta\,e_1,\quad
Ye_j=e_j\ (2\leq j\leq a).
\]

Here \(X\) has one-dimensional kernel and \(Y\) is invertible. A product equal to zero must contain at least \(a+1\) occurrences of \(X\): each factor \(X\) decreases rank by at most one, and \(Y\) never decreases it. Also a zero product must contain at least \(n\) occurrences of \(Y\). To see this, apply the word to \(e_0\): after every occurrence of \(X\) the surviving vector is a scalar multiple of \(e_0\), and the word block \(1^j0\), acting as \(XY^j\), multiplies this scalar by \(\cos(j\theta)\). Without a vanishing cosine the product cannot annihilate \(e_0\). The first nonnegative integer \(j\) with \(\cos(j\theta)=0\) is \(n\).

It follows that no zero word has length less than \(a+n+1\). At that length, a zero word would have exactly \(a+1\) zero letters and exactly \(n\) one letters. All one letters must constitute a single run followed by a zero, so the word must be \(0^k1^n0^{a+1-k}\) for some \(0\leq k\leq a\). If \(k<a\), its action on \(e_{k+1}\) is nonzero: \(X^ke_{k+1}=e_1\), \(Y^ne_1=-e_0\), and every remaining \(X\) fixes \(e_0\). On the other hand, \(X^a(U)=\mathbb R e_0\), \(Y^ne_0=e_1\), and \(Xe_1=0\). Thus

\[
XY^nX^a=0,
\]

and \(0^a1^n0\) is the **only** zero product of minimum length. This proves that the minimum real matrix dimension is at most \(a+1\), and the rank argument above gives the reverse inequality for any real-matrix realization with a unique shortest zero word.

**3. Quantum realization.** Take \(d=\lceil\sqrt{a+2}\rceil\), so that the real space of traceless Hermitian \(d\times d\) matrices has dimension \(d^2-1\geq a+1\). Embed \(U\) in that space and extend \(X,Y\) by zero on a complementary real subspace, obtaining real-linear maps \(L_0,L_1\). For all sufficiently small positive \(\varepsilon\), the trace-preserving, Hermiticity-preserving maps

\[
A_b(\rho)=\frac{I}{d}+\varepsilon L_b\!\left(\rho-\frac{I}{d}\right),\quad b\in\{0,1\},
\]

extend to complex-linear, completely positive channels by \(A_b(Z)=(\operatorname{tr}Z)I/d+\varepsilon L_b(Z-(\operatorname{tr}Z)I/d)\), with \(L_b\) complexified from traceless Hermitians. Their Choi matrices are the strictly positive Choi matrix of the completely depolarizing channel plus \(\varepsilon\) times a fixed Hermitian perturbation. Choose \(\rho_0=I/d+\delta e_a\) for sufficiently small \(\delta>0\). The reachable difference span is exactly the embedded \(U\): the powers \(X^j e_a=e_{a-j}\), \(0\leq j<a\), produce \(e_a,\ldots,e_1\), while \(Y e_1\) has a nonzero \(e_0\)-component; also \(X^ae_a=0\) makes \(I/d\) reachable. Every reachable state lies in \(I/d+U\). The induced action of a word on differences is a nonzero scalar \(\varepsilon^{|w|}\) times the corresponding real matrix product. Consequently the unique shortest synchronizing word is precisely \(0^a1^n0\).

Combining both bounds proves the formula for all \(a,n\geq1\).

## Verification

Run `python3 verify.py` using Python 3 and its standard library. The script independently enumerates all binary words through length \(a+n+1\) for each of the 40 parameter pairs \(1\leq a\leq8\), \(1\leq n\leq5\), evaluates the constructed real matrix products, and tests that only \(0^a1^n0\) vanishes at the first possible length. It also checks the Hilbert-dimension rounding for \(1\leq a\leq32\). The recorded output is in `verification_output.txt`. These finite floating-point checks are auxiliary consistency evidence; the rank, cosine, and Choi arguments above give the exact all-parameter proof.

## Relationship to prior work

Lee, Lee, and Kjos-Hanssen [1] introduce this specific quantum Černý invariant, prove its general upper bound \(\operatorname{qc}(w)\leq\lceil\sqrt{|w|+1}\rceil\), prove \(\operatorname{qc}(0^m)=\lceil\sqrt{m+1}\rceil\), and establish the case \(\operatorname{qc}(01^n0)=2\), citing earlier work by Lakshmanan. Their discussion explicitly leaves general qubit realizability open. The present result determines an additional two-parameter family and proves the sharp boundary at a doubled leading zero run for qubits. It is **not** implied by the general length-based upper bound, which increases with \(n\), nor by the constant-word calculation, which does not provide a mixed nilpotent/rotation witness. The earlier qutrit construction of Kjos-Hanssen and Lakshmanan [2] concerns arbitrarily long synchronizing words for fixed three-dimensional channels; its displayed construction and Theorem 11 do not give this exact two-parameter optimum.

## Limitations

The claim is specific to the mixed-target quantum Černý definition and the word family \(0^a1^n0\) for positive integer parameters. The perturbative quantum channels need not synchronize all density matrices; only the reachable set from the chosen initial state is required. The proof does not determine the pure-target complexity, quantum complexity of arbitrary words, or stability under approximate synchronization. The source comparison does not certify exhaustive priority over unpublished or unindexed material, including any inaccessible dissertation text.

## References

[1] P. H. Lee, P.-Y. Lee, and B. Kjos-Hanssen, *Quantum Černý complexity of binary words*, arXiv:2609.40154, first submitted 2026-09-30. https://arxiv.org/abs/2609.40154

[2] B. Kjos-Hanssen and S. Lakshmanan, *Unbounded length minimal synchronizing words for quantum channels over qutrits*, arXiv:2603.00861, first submitted 2026-03-01. https://arxiv.org/abs/2603.00861
