# Correct super-Hilbert four-term von Neumann–Jordan profile on \(\ell_q\)
## Finding
For a real sequence space \(X=\ell_q(I)\) with \(|I|\ge2\), \(2\le q<\infty\), and \(\lambda\in[0,1]\), define
\[
C'''_{\mathrm{NJ}}(\lambda,X)=\sup_{x,y\in S_X}\frac12\Bigl(\|\lambda x+(1-\lambda)y\|^2+\|\lambda x-(1-\lambda)y\|^2+\lambda(1-\lambda)\|x-y\|^2+\lambda(1-\lambda)\|x+y\|^2\Bigr).
\]
Writing \(r=|2\lambda-1|\), the exact value is
\[
C'''_{\mathrm{NJ}}(\lambda,\ell_q(I))=2^{-2/q}\left((1+r^q)^{2/q}+1-r^2\right).
\]
Equivalently,
\[
C'''_{\mathrm{NJ}}(\lambda,\ell_q(I))=2^{-2/q}(1+|2\lambda-1|^q)^{2/q}+2^{2-2/q}\lambda(1-\lambda).
\]
The value is attained by the two-coordinate pair
\[
x=2^{-1/q}(e_1+e_2),\qquad y=2^{-1/q}(e_1-e_2).
\]
This gives a correction to the \(q\ge2\) formula in Example 3.1 of the current revision of arXiv:2110.15741.

## Assumptions and scope
The scalars are real, \(I\) has at least two elements, and \(2\le q<\infty\). The statement uses exactly the unit-sphere definition displayed above. No assertion is made here for \(q=\infty\), for other Banach spaces, or for differently normalized von Neumann–Jordan constants.

## Proof
Fix \(x,y\in S_{\ell_q(I)}\). Put
\[
A=\|\lambda x+(1-\lambda)y\|_q,\qquad B=\|\lambda x-(1-\lambda)y\|_q.
\]
For \(q\ge2\), Hanner's inequality in \(\ell_q\) has the reversed form
\[
\|u+v\|_q^q+\|u-v\|_q^q\le(\|u\|_q+\|v\|_q)^q+|\|u\|_q-\|v\|_q|^q.
\]
Applying it to \(u=\lambda x\) and \(v=(1-\lambda)y\) gives
\[
A^q+B^q\le1+r^q.
\]
For nonnegative \(a,b\), comparison of the two-dimensional \(\ell_2\) and \(\ell_q\) norms gives
\[
a^2+b^2\le2^{1-2/q}(a^q+b^q)^{2/q}.
\]
Hence
\[
A^2+B^2\le2^{1-2/q}(1+r^q)^{2/q}.
\]
Applying Hanner's inequality again, now to the unit vectors \(x,y\), yields
\[
\|x+y\|_q^q+\|x-y\|_q^q\le2^q,
\]
and therefore
\[
\|x+y\|_q^2+\|x-y\|_q^2\le2^{3-2/q}.
\]
Substitution into the defining expression gives
\[
C'''_{\mathrm{NJ}}(\lambda,\ell_q(I))\le2^{-2/q}(1+r^q)^{2/q}+2^{2-2/q}\lambda(1-\lambda).
\]
Since \(4\lambda(1-\lambda)=1-r^2\), this is the stated bound.

For sharpness, take
\[
x=2^{-1/q}(e_1+e_2),\qquad y=2^{-1/q}(e_1-e_2).
\]
Then \(x,y\in S_{\ell_q(I)}\), the two weighted norms are equal to
\[
2^{-1/q}(1+r^q)^{1/q},
\]
and both \(\|x+y\|_q\) and \(\|x-y\|_q\) equal \(2^{1-1/q}\). Thus equality holds simultaneously in both upper bounds, proving the formula.

## Verification
At \(q=2\), the formula reduces identically to \(1\), as required by the parallelogram law. At \(\lambda=0\) or \(\lambda=1\), it also reduces to \(1\). At \(\lambda=1/2\), it becomes \(2^{1-2/q}\), the expected unit-sphere von Neumann–Jordan value for \(\ell_q\).

A decisive check against the printed super-Hilbert formula is \(q=4\), \(\lambda=1/4\). The theorem gives
\[
C'''_{\mathrm{NJ}}(1/4,\ell_4)=\frac{\sqrt{17}+3}{4\sqrt2}.
\]
Its square is \((13+3\sqrt{17})/16\). The formula printed in Example 3.1 gives \(\sqrt7/2\), whose square is \(7/4\). Since \(\sqrt{17}<5\), the sharp Hanner upper bound is strictly below the printed value. The bundled `verify.py` replays this numerical/algebraic checkpoint and the equality witness; it is a finite consistency check, not the proof of the theorem.

## Relationship to prior work
The current revision of Yuxin Wang, Qi Liu, Qian Li, Qichuan Ni, Zhijian Yang, Muhammad Sarfraz, and Yongjin Li, arXiv:2110.15741, defines \(C'''_{\mathrm{NJ}}\) by the unit-sphere supremum above and gives a different claimed exact formula for \(\ell_q\), \(q\ge2\), in Example 3.1. Its proof introduces an auxiliary scale \(a\in[0,1]\) and then optimizes over \(a\). That extra optimization is not present in the defining unit-sphere supremum. The argument above works directly at the defined scale and gives a matching upper bound and witness.

The critical inequality is the classical Hanner inequality for \(L^p\) and \(\ell_p\), with the direction reversed for \(p\ge2\). A separate exact result for the same four-term invariant on the sub-Hilbert range \(1\le q<2\) has a different formula and does not cover the range proved here.

## Limitations
The proof is specific to real \(\ell_q\) and uses the sharp Hanner inequality. It does not classify all equality pairs. It corrects the exact value of the displayed unit-sphere invariant; it does not assess unrelated results of the source. No independent audit has been performed.

## References
1. Y. Wang, Q. Liu, Q. Li, Q. Ni, Z. Yang, M. Sarfraz, and Y. Li, *Novel constants based on the generalization of Von Neumann-Jordan constant*, arXiv:2110.15741, first submitted 2021-10-29; current revision inspected at Definition/Section 3 and Example 3.1.
2. O. Hanner, *On the uniform convexity of \(L^p\) and \(\ell^p\)*, Arkiv för Matematik 3 (1956), 239–244, DOI 10.1007/BF02589410.
