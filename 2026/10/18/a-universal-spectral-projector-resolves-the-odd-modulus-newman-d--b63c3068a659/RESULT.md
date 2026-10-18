# A universal spectral projector resolves the odd-modulus Newman digit-sum conjecture

## Finding
For each odd integer \(n\ge3\), set \(b=n-1\). Let \(s_b(r)\) denote the ordinary digit sum of a nonnegative integer \(r\) written in base \(b\). Define, for every integer \(x\ge0\) and each residue \(i\in\{0,1,\ldots,n-1\}\),
\[
S_{n,i}(x)=\sum_{\substack{0\le r<x\\r\equiv i\pmod n}}(-1)^{s_b(r)}.
\]
Then the following identity holds for **every** such \(n,i,x\):
\[
\boxed{\sum_{j=0}^{(n-1)/2}(-1)^j\binom{n}{2j+1}S_{n,i}(b^{2j}x)
=\sum_{k=0}^{n-1}S_{n,k}(x).}
\tag{1}
\]
In particular, the right-hand side is \(0\) for even \(x\) and is \((-1)^{s_b(x-1)}\) for odd \(x\). Equation (1) supplies a uniform proof of the two conjectural identities (15) and (74) in Shevelev and Moses, *A family of digit functions with large periods* (2012): the first for residue \(i=0\) and the second for all residues. It also includes \(x=0\).

The underlying stronger matrix identity is
\[
\boxed{P_n(B^2)=J_n,}\qquad
P_n(Y)=\sum_{j=0}^{(n-1)/2}(-1)^j\binom{n}{2j+1}Y^j,
\tag{2}
\]
where \(J_n\) is the all-one matrix and \(B\) is the explicit integer matrix defined below.

## Assumptions and scope
Throughout, \(n\) is an arbitrary odd integer at least \(3\), not necessarily prime. The base \(b=n-1\) is even and at least \(2\); \(x\) is an integer, not a real cutoff; all residue indices range over \(0,\ldots,n-1\). Empty sums at \(x=0\) are \(0\). No asymptotic limit, numerical hypothesis, or assumption on the prime factors of \(n\) is used.

For any integer \(t\), let \(\bar t\) be its least nonnegative residue modulo \(n\). Define \(a_0,\ldots,a_{n-1}\) by \(a_d=(-1)^d\) for \(0\le d\le n-2\) and \(a_{n-1}=0\). Put
\[
B_{r,s}=a_{\overline{r+s}},\qquad 0\le r,s<n.
\]
Thus \(B\) is a symmetric, integral, explicitly specified matrix.

## Proof
**1. Digit concatenation.** Write the residue-sum column vector as
\(\mathbf S(x)=(S_{n,0}(x),\ldots,S_{n,n-1}(x))^{\mathsf T}\).
Every integer in \([0,bx)\) has a unique decomposition \(r=bu+d\) with \(0\le u<x\) and \(0\le d<b\). Its digit-sign is \((-1)^{s_b(u)+d}\), and since \(b\equiv-1\pmod n\), its residue is \(d-u\pmod n\). Therefore
\[
S_{n,r}(bx)=\sum_{s=0}^{n-1}
\left(\sum_{\substack{0\le d<b\\d\equiv r+s\pmod n}}(-1)^d\right)S_{n,s}(x)
=\sum_{s=0}^{n-1}B_{r,s}S_{n,s}(x).
\]
There is at most one admissible digit for each residue, as \(0\le d\le n-2\). We have proved \(\mathbf S(bx)=B\mathbf S(x)\), and iteration yields
\[
\mathbf S(b^{2j}x)=(B^2)^j\mathbf S(x)\qquad(j\ge0).
\tag{3}
\]

**2. Fourier action of the digit matrix.** Work over \(\mathbb C\). For each root \(z\) of \(z^n=1\), let \(v_z=(1,z,\ldots,z^{n-1})^{\mathsf T}\). These \(n\) vectors form a basis. Put
\[
A(z)=\sum_{d=0}^{n-2}(-z)^d.
\]
The substitution \(d\equiv r+s\pmod n\) gives, coordinate by coordinate,
\[
(Bv_z)_r=\sum_{s=0}^{n-1}a_{\overline{r+s}}z^s
=z^{-r}A(z),\quad\text{hence }Bv_z=A(z)v_{z^{-1}}.
\tag{4}
\]
Thus \(B^2v_z=\lambda_zv_z\), with \(\lambda_z=A(z)A(z^{-1})\).

For \(z=1\), the \(n-1\) alternating terms in \(A(1)\) cancel because \(n-1\) is even. Hence \(\lambda_1=0\).
For \(z\ne1\), oddness of \(n\) ensures \(z\ne-1\), so the finite geometric progression and \(z^n=1\) give
\[
A(z)=\frac{1-z^{-1}}{1+z},\qquad
A(z^{-1})=\frac{1-z}{1+z^{-1}},\qquad
\lambda_z=-\left(\frac{z-1}{z+1}\right)^2.
\tag{5}
\]

**3. The spectral projector.** Let \(w=(z-1)/(z+1)\) for a nontrivial \(n\)th root \(z\). As \(w\ne0\), the odd-binomial expansion yields
\[
\begin{aligned}
P_n(-w^2)
&=\sum_{j=0}^{(n-1)/2}\binom{n}{2j+1}w^{2j}\\
&=\frac{(1+w)^n-(1-w)^n}{2w}\\
&=\frac{2^{n-1}(z^n-1)}{(z-1)(z+1)^{n-1}}=0.
\end{aligned}
\tag{6}
\]
Thus \(P_n(B^2)v_z=0\) for all nontrivial \(n\)th roots \(z\). On the constant character \(v_1\), equation (5) is replaced by \(\lambda_1=0\) and \(P_n(0)=\binom n1=n\), so \(P_n(B^2)v_1=nv_1\). The all-one matrix \(J_n\) has precisely these actions: it multiplies \(v_1\) by \(n\) and annihilates all other characters. Equality on a basis establishes the integer matrix identity (2) for every odd \(n\ge3\).

**4. Recovering the conjecture.** By (3) and (2),
\[
\sum_{j=0}^{(n-1)/2}(-1)^j\binom n{2j+1}
\mathbf S(b^{2j}x)
=P_n(B^2)\mathbf S(x)=J_n\mathbf S(x).
\]
Every coordinate of the last vector equals \(\sum_{k=0}^{n-1}S_{n,k}(x)\), proving (1), including the endpoint \(x=0\).

Finally, the sum across all residue classes is \(\sum_{0\le r<x}(-1)^{s_b(r)}\). Because \(b\) is even, each adjacent pair \(r=2u,2u+1\) has opposite digit-signs: adding one to an even integer changes only its even final base-\(b\) digit to the following odd digit. Pairwise cancellation gives the stated explicit parity formula. This completes the proof.

## Verification
The accompanying self-contained `verify_newman_projector.py` uses exact integer arithmetic. It checks identity (2) for each odd \(n\) from \(3\) through \(25\) (twelve complete matrix tests), checks the digit-step transition and all residue coordinates for 144 pairs \((n,x)\) across moduli \(3,5,7,9\), and independently enumerates the finite sums of (1) at a further range of small arguments. It prints `VERIFY_OK` if all tests pass. Run with a standard Python 3 interpreter, without third-party dependencies.

These finite checks corroborate the algebra; the infinite statement follows only from the Fourier-basis proof above. All matrices, hypotheses, and intermediate identities needed for the proof are defined here.

## Relationship to prior work
Shevelev and Moses (arXiv:1209.5705, submitted September 24, 2012) introduced the functions in (1). Their equation (15) proposed the \(i=0\) identity, reporting proofs for \(n=3,5\) and finite tests at other odd moduli. Their Section 10, equation (74), explicitly conjectured the all-residue form; their Section 4 recorded a general digit-step system, equivalent to the action of \(B\) above, but did not prove (74).

In their earlier *Tangent power sums and their applications* (arXiv:1207.0404, first submitted June 29, 2012), the same authors derived related root-of-unity and tangent-power formulas, including the odd-binomial annihilating polynomial (their Section 3, equation (11)). These polynomial roots are deliberately not claimed as new. The proof here uses the exact *matrix identity* \(P_n(B^2)=J_n\) to connect the known spectral polynomial with the full interval-sensitive residue vector. That bridge proves both explicitly conjectural statements uniformly for all odd moduli and all cutoffs.

## Limitations
Only odd moduli \(n\ge3\), the paired base \(n-1\), and integer cutoffs are claimed. Nothing here establishes a corresponding identity for even moduli or unrelated bases, or an independent audit of originality. Although targeted literature and research-record searches did not identify an earlier general proof of equation (74), an unindexed derivation or a more general prior matrix theorem could provide overlapping coverage. The statements in the original paper were conjectural, not newly formulated here; the contribution is a complete uniform proof. A separate independent mathematical review has not yet been performed.

## References
1. V. Shevelev and P. J. C. Moses, *A family of digit functions with large periods*, arXiv:1209.5705 (first submitted 2012-09-24), especially Section 1 equation (15), Section 4 equation (38), and Section 10 equation (74). https://arxiv.org/html/1209.5705v3
2. V. Shevelev and P. J. C. Moses, *Tangent power sums and their applications*, arXiv:1207.0404 (first submitted 2012-06-29), especially Sections 2–3, equations (3)–(4) and (11). https://arxiv.org/html/1207.0404v6
