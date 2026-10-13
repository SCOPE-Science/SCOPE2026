# Complete fixed-space spectrum of automorphisms of the three-dimensional Heisenberg Lie algebra
## Finding
Let \(q\) be a prime power and let \(H_3(\mathbb F_q)\) have basis \(x,y,z\) with \([x,y]=z\). If \(N_d(q)\) counts automorphisms with fixed-space dimension \(d\), then
\[
N_0(q)=q^3(q+1)(q-2)^2,
\]
\[
N_1(q)=q(2q^4-q^3-4q^2-q+1),
\]
\[
N_2(q)=(q^2-1)(q+1),\qquad N_3(q)=1.
\]
These four values exhaust the automorphism group. Consequently
\[
\frac{1}{|\operatorname{Aut}(H_3(\mathbb F_q))|}
\sum_{\phi}q^{\dim\operatorname{Fix}(\phi)}=3,
\]
which is the number of automorphism orbits on the underlying elements.

## Assumptions and scope
The field is an arbitrary finite field \(\mathbb F_q\), including characteristic two. The result concerns ordinary \(\mathbb F_q\)-linear Lie-algebra automorphisms of the three-dimensional Heisenberg Lie algebra, not automorphisms of the corresponding Heisenberg group and not derivations. A fixed subspace is the kernel of \(\phi-I\).

Every automorphism preserves the center \(\mathbb F_q z\). Its induced action on \(H_3/\mathbb F_qz\) is a matrix \(A\in\operatorname{GL}_2(\mathbb F_q)\), and bracket preservation forces the action on \(z\) to be multiplication by \(\delta=\det A\). Conversely, arbitrary central shifts of the images of \(x\) and \(y\) are allowed. Thus every automorphism is uniquely represented by a pair \((A,w)\), with \(A\in\operatorname{GL}_2(\mathbb F_q)\) and \(w\in(\mathbb F_q^2)^*\), and
\[
|\operatorname{Aut}(H_3(\mathbb F_q))|=q^2|\operatorname{GL}_2(\mathbb F_q)|=q^3(q-1)^2(q+1).
\]

## Proof
Write an element as \((v,t)\in\mathbb F_q^2\oplus\mathbb F_qz\). For the automorphism associated with \((A,w)\), the fixed-point equations are
\[
(A-I)v=0,\qquad w(v)+(\delta-1)t=0,
\]
where \(\delta=\det A\). Put \(K=\ker(A-I)\) and \(r=\dim K\).

If \(\delta\ne1\), the second equation determines \(t\) uniquely for every \(v\in K\). Hence the fixed-space dimension is exactly \(r\), independently of \(w\). If \(\delta=1\), then \(t\) is free and the second equation becomes \(w(v)=0\), so
\[
\dim\operatorname{Fix}(\phi)=1+\dim(K\cap\ker w).
\]

It remains to count the five possible strata of \(A\). They are
\[
\#\{A:\delta\ne1,r=0\}=q(q+1)(q-2)^2,
\]
\[
\#\{A:\delta\ne1,r=1\}=q(q+1)(q-2),
\]
\[
\#\{A:\delta=1,r=0\}=q(q^2-q-1),
\]
\[
\#\{A:\delta=1,r=1\}=q^2-1,
\]
and one matrix has \(\delta=1,r=2\), namely \(A=I\).

For the determinant-one strata, the last two counts come from the identity and the single nonidentity unipotent conjugacy type in \(\operatorname{SL}_2(\mathbb F_q)\); altogether exactly \(q^2\) elements of \(\operatorname{SL}_2(\mathbb F_q)\) have eigenvalue \(1\), leaving \(q(q^2-q-1)\) with no fixed vector. For \(\delta\ne1\), an element with a one-dimensional fixed space has eigenvalues \(1\) and \(\delta\ne1\); summing the corresponding split semisimple conjugacy classes gives \(q(q+1)(q-2)\), and subtraction from all matrices with determinant different from one gives \(q(q+1)(q-2)^2\).

Now count the covectors \(w\). In the \(\delta=1,r=1\) stratum, exactly \(q\) covectors vanish on the one-dimensional space \(K\), while \(q^2-q\) do not. For \(A=I\), the zero covector gives fixed-space dimension \(3\) and the other \(q^2-1\) covectors give dimension \(2\). Combining these contributions yields the stated formulas for \(N_0,N_1,N_2,N_3\).

Finally, Burnside's lemma gives
\[
\frac{N_0+qN_1+q^2N_2+q^3N_3}{q^3(q-1)^2(q+1)}=3.
\]
Directly, the three element-orbits are \(\{0\}\), the nonzero central elements, and the noncentral elements, confirming the average.

## Verification
The proof is symbolic and valid for every prime power \(q\). The accompanying `verify.py` independently enumerates the full automorphism group for \(q=2,3,4,5,7\), using an explicit model of \(\mathbb F_4\) in the extension-field case. For each automorphism it computes the rank of \(\phi-I\), checks all four multiplicity formulas, checks the total automorphism-group order, and checks that the Burnside average is exactly \(3\). A fresh replay ends with `VERIFY_OK`.

The checks include \(q=2\), where the fixed-point-free stratum is empty, and \(q=4\), so the characteristic-two and non-prime-field boundaries are both exercised. The finite enumerations corroborate but do not prove the universal formulas.

## Relationship to prior work
Fisher, Gray, and Hydon give the automorphism matrices for the nilpotent three-dimensional real Lie algebra \(A_{3,1}\), which is the real Heisenberg Lie algebra. Their displayed matrix form supplies the classical structural analogue, but their paper does not count finite-field fixed-space dimensions. The present proof derives the same block form directly over every finite field before performing the finite-field count.

A published published-finding corpus finding gives exactly the fixed-point-free fiber
\[
N_0(q)=q^3(q+1)(q-2)^2.
\]
That result is therefore a strict special case of the complete spectrum recorded here and is credited rather than claimed as new. Searches for fixed-space distributions, theta-value formulations, and exact numbers of automorphisms fixing \(q^d\) elements did not locate the remaining three fibers or the complete distribution for this Lie algebra.

Liu and Tang's 2018 paper is directly about automorphism groups of Heisenberg Lie (super)algebras and is therefore a particularly relevant same-object comparison. Its accessible full article works over a commutative ring and constructs inner, central, and involutionary automorphism subgroups. It does not enumerate fixed points or fixed-space dimensions over finite fields, so its results do not imply the spectrum proved here.

General literature on fixed-point-free automorphisms of Lie algebras studies structural consequences of regular automorphisms rather than this exact finite-field distribution. Literature on theta-values of finite groups motivates the naturality of counting automorphisms by fixed-set size but concerns groups rather than the present Lie algebra.

## Limitations
The result is specific to the three-dimensional Heisenberg Lie algebra. It does not give the fixed-space spectrum for higher-dimensional Heisenberg Lie algebras, where the quotient action is symplectic-similitude rather than arbitrary two-dimensional general linear. The literature search is bounded; an equivalent finite-field count could exist under different terminology. The closest same-object automorphism-group paper inspected does not enumerate finite-field fixed spaces, but this does not exclude all unlocated literature. The fixed-point-free fiber is already known and is included only to make the complete distribution explicit.

## References
1. D. J. Fisher, R. J. Gray, and P. E. Hydon, *Automorphisms of real Lie algebras of dimension five or less*, arXiv:1303.3376; Journal of Physics A 46 (2013), 225204, DOI 10.1088/1751-8113/46/22/225204.
2. published-finding corpus, *Exact fixed-point-free automorphism count for the three-dimensional Heisenberg Lie algebra*, record `2026/10/4/SCOPE-exact-fixed-point-free-automorphism-count-for-the-three-dimensio--17f0de4cb789`.
3. J. Zha, *Fixed-point-free Automorphisms of Lie Algebras*, Acta Mathematica Sinica (1989), DOI 10.1007/BF02107627.
4. E. I. Khukhro and P. V. Shumyatskii, *Fixed points of automorphisms of Lie rings and locally finite groups*, Algebra and Logic 34 (1996), 395–405, DOI 10.1007/BF00739335.
5. J. Liu and Z. Tang, *The automorphism groups of Heisenberg Lie (super)algebras*, 2018, DOI 10.13548/J.SXZZ.20170518.003.
