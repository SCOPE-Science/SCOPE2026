# Exact distribution of nonzero idempotents in random two-dimensional perfect evolution algebras

## Finding
Let \(q\) be an arbitrary prime power, choose \(A\) uniformly from \(\operatorname{GL}_2(\mathbb F_q)\), and let
\[
N(A)=\#\{x\in\mathbb F_q^2\setminus\{0\}:A(x_1^2,x_2^2)^T=x\}.
\]
This is the number of nonzero idempotents of the perfect two-dimensional evolution algebra with structure matrix \(A\), with a specified natural basis. Its entire distribution is as follows. In every case, \(N\in\{0,1,2,3\}\) and
\[
\boxed{\Pr[N=0]=\frac13}.
\]
If \(q\) is even, the probabilities in order \(N=0,1,2,3\) are
\[
\boxed{\left(\frac13,\frac12,0,\frac16\right)}.
\]
If \(q\) is odd, they are
\[
\boxed{\left(\frac13,\frac{q^2+1}{2q(q+1)},\frac{q-1}{q(q+1)},\frac{q^2-2q+3}{6q(q+1)}\right)}.
\]
The even-characteristic distribution is **exactly** the fixed-point-count law of a uniform permutation in \(S_3\) for every field size, not merely asymptotically. For odd \(q\), letting \(\delta_q=(q-1)/(q(q+1))\), the distribution differs from the \(S_3\) law by \(\delta_q(0,-1/2,1,-1/2)\), a sharp finite-field correction.

Equivalently, exactly \(|\operatorname{GL}_2(\mathbb F_q)|/3=q(q-1)^2(q+1)/3\) invertible structure matrices have no nonzero idempotent. In even characteristic exactly two nonzero idempotents never occur; in odd characteristic all four possible values occur.

## Assumptions and scope
An evolution algebra is a commutative algebra with basis \(e_1,e_2\) satisfying \(e_1e_2=0\). Its matrix \(A\) acts on the vector of squared coordinates, so idempotency is \(Ax^{[2]}=x\). A matrix is perfect precisely when it is invertible. This theorem uses the *uniform distribution on invertible matrices relative to a chosen ordered natural basis*: it is not a uniform distribution on isomorphism classes. All fields \(\mathbb F_q\) and both characteristics are covered, including \(q=2\) and nonprime finite fields. Zero is excluded from \(N\) and is always an idempotent. No independence assumptions on individual candidate idempotents are made.

## Proof
**1. Projective reduction and the cubic bound.** For \([v]\in\mathbb P^1(\mathbb F_q)\), define
\[
\phi_A([v])=[Av^{[2]}].
\]
Since \(A\) is invertible, \(Av^{[2]}\ne0\) for every \(v\ne0\). The projective direction \([v]\) is fixed if and only if \(Av^{[2]}=\lambda v\) for some unique \(\lambda\ne0\). Then the unique nonzero idempotent on this line is \(\lambda^{-1}v\), because \(A(\lambda^{-1}v)^{[2]}=\lambda^{-1}v\). Conversely every nonzero idempotent yields a fixed line. Thus \(N(A)\) is exactly the number of rational fixed points of \(\phi_A\).

Write \(A=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\). A fixed line \([X:Y]\) satisfies the homogeneous cubic equation
\[
\det\!\left(\begin{smallmatrix}X&aX^2+bY^2\\Y&cX^2+dY^2\end{smallmatrix}\right)
=cX^3-aX^2Y+dXY^2-bY^3=0.
\]
This homogeneous cubic is not the zero polynomial, since \(A\) is invertible. It has at most three distinct projective zeros over any field. Therefore \(0\le N(A)\le3\).

**2. Simultaneous fixed-line probabilities.** The map \(s:\mathbb P^1(\mathbb F_q)\to\mathbb P^1(\mathbb F_q)\), \(s([v])=[v^{[2]}]\), is the coordinatewise squaring map. For any ordered \(k\)-tuple of distinct projective points \(P_1,\dots,P_k\), with \(1\le k\le3\), the conditions that \(A\) fixes all these points mean that its projective class \([A]\in\operatorname{PGL}_2(\mathbb F_q)\) sends \(s(P_i)\) to \(P_i\). If the \(s(P_i)\) are not distinct, no invertible \(A\) can satisfy the conditions. If they are distinct, sharp three-transitivity of \(\operatorname{PGL}_2(\mathbb F_q)\) implies the proportion of suitable matrices is
\[
\frac{1}{(q+1)_k},\qquad (q+1)_k=(q+1)q\cdots(q+2-k).
\]
For \(k=1,2\) this follows as well by transitivity on ordered distinct points and equal stabilizer sizes; for \(k=3\) the stabilizer is trivial. Since \(|\operatorname{PGL}_2(\mathbb F_q)|=q(q^2-1)=(q+1)_3\), all formulas hold when \(q=2\).

**3. Squaring collisions.** For even \(q\), squaring is a field automorphism, so \(s\) permutes all \(q+1\) projective points. For odd \(q\), its fibers have sizes \(1,1\) at \(0,\infty\), and size \(2\) at each of the \((q-1)/2\) nonzero square values. Hence exactly \(q-1\) ordered pairs of distinct points have the same \(s\)-image.

Let \(T_k\) count ordered \(k\)-tuples of distinct projective points with pairwise distinct squaring images. For even \(q\),
\[
(T_1,T_2,T_3)=(q+1,(q+1)q,(q+1)q(q-1)).
\]
For odd \(q\),
\[
\begin{aligned}
T_1&=q+1,\\
T_2&=(q+1)q-(q-1)=q^2+1,\\
T_3&=(q+1)q(q-1)-3(q-1)^2\\
&=(q-1)(q^2-2q+3).
\end{aligned}
\]
For the third count, select one of three positions for the colliding pair, one of the \(q-1\) ordered distinct pairs sharing an image, and one of the \(q-1\) remaining points. No triple has two different colliding pairs because every squaring fiber has size at most two; therefore there is no double counting.

**4. Factorial moments and inversion.** Write \(F_k=\mathbb E[(N)_k]\), with \((N)_k=N(N-1)\cdots(N-k+1)\). Step 2 gives \(F_k=T_k/(q+1)_k\) for \(k=1,2,3\). In particular \(F_1=1\); when \(q\) is even, \(F_2=F_3=1\), and when \(q\) is odd,
\[
F_2=\frac{q^2+1}{q(q+1)},\qquad
F_3=\frac{q^2-2q+3}{q(q+1)}.
\]
Because \(N\in\{0,1,2,3\}\), its distribution is uniquely determined by these factorial moments:
\[
\begin{aligned}
\Pr[N=3]&=F_3/6,\\
\Pr[N=2]&=(F_2-F_3)/2,\\
\Pr[N=1]&=F_1-F_2+F_3/2,\\
\Pr[N=0]&=1-F_1+F_2/2-F_3/6.
\end{aligned}
\]
Substitution yields the displayed probabilities. In both characteristics, the last expression simplifies to exactly \(1/3\). All denominators are nonzero for \(q\ge2\). This proves the theorem.

## Verification
Execute `python3 verify.py` to enumerate all invertible \(2\times2\) matrices over \(\mathbb F_q\) for \(q\in\{2,3,4,5,7,8,9\}\), with explicit extension-field arithmetic, and compare every frequency with the formula. Execute `python3 verify_direct.py` for a separately implemented direct census of all solutions \(Ax^{[2]}=x\) over \(q\in\{2,3,5,7\}\). Both programs use only Python's standard library. Their expected terminal markers are `VERIFY_OK` and `DIRECT_VERIFY_OK`. The finite checks include extension fields of characteristic two and three; the proof, rather than finite enumeration, establishes all prime powers.

## Relationship to prior work
Kaygorodov, Martín González, and Viruel (2026, Remark 23) prove that the expected number of nonzero idempotents of a uniformly random perfect evolution algebra is one in every dimension; their existence theorem additionally constructs idempotent-free examples. Their Conjecture 2 predicts an asymptotic symmetric-group fixed-point law; the present theorem gives its exact dimension-two finite-field refinement. Those results alone do not give the frequencies of the four possible idempotent counts in dimension two. The present result obtains the complete law using the third factorial moment and the sharp three-transitivity of projective transformations. Wei and Zou (2023) enumerate *isomorphism classes* of perfect evolution algebras, a different counting measure. The projective formulation also shows why the characteristic-two and odd-characteristic laws differ: coordinatewise squaring collides on pairs of projective points only in odd characteristic.

## Limitations
The probabilities count labeled structure matrices relative to a specified natural basis, not algebra isomorphism classes. The theorem is specifically two-dimensional and does not determine higher-dimensional distributions. It does not classify automorphism groups of the algebras or the field extensions of their idempotent coordinates. Historical priority beyond the inspected sources has not been independently established.

## References
- I. Kaygorodov, C. Martín González, and A. Viruel, *Evolution algebras: a survey of results and a list of open problems* (2026), arXiv:2610.22248v1, especially §2.1.5 and Remark 23. https://arxiv.org/abs/2610.22248
- Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras* (2023), arXiv:2310.12368v1. https://arxiv.org/abs/2310.12368
