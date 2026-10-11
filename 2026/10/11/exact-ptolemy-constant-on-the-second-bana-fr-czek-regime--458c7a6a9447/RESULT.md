# Exact Ptolemy constant on the second Banaś--Frączek regime
## Finding
For every real \(\lambda>\sqrt2\), let \(R_\lambda^2=(\mathbb R^2,N_\lambda)\) be the Banaś--Frączek plane
\[
N_\lambda(x_1,x_2)=\max\left\{\lambda|x_1|,\sqrt{x_1^2+x_2^2}\right\}.
\]
Then
\[
C_{\mathrm{Pt}}(R_\lambda^2)=2\sqrt{1-\lambda^{-2}}.
\]
Writing \(t_\lambda=\sqrt{\lambda^2-1}\), the triple
\[
x=(1,t_\lambda),\qquad y=(1,-t_\lambda),\qquad z=(2,0)
\]
attains this Ptolemy ratio exactly.

The formula joins continuously to the already known first-regime value at \(\lambda=\sqrt2\), where both expressions equal \(\sqrt2\), and tends to \(2\) as \(\lambda\to\infty\).

## Assumptions and scope
The scalar field is real and the dimension is exactly two. The Ptolemy constant is
\[
C_{\mathrm{Pt}}(X)=
\sup
\frac{\|x-y\|\,\|z\|}
{\|x-z\|\,\|y\|+\|z-y\|\,\|x\|},
\]
where the supremum ranges over nonzero pairwise distinct \(x,y,z\in X\).

The theorem covers only \(\lambda>\sqrt2\). The endpoint \(\lambda=\sqrt2\) is mentioned only to show continuity with the complementary regime and is not part of the new quantified claim.

## Proof
Write
\[
E(v)=\sqrt{v_1^2+v_2^2},
\qquad
F(v)=\lambda|v_1|,
\qquad
N_\lambda(v)=\max\{E(v),F(v)\}.
\]
Put
\[
c=\frac{\lambda^2}{2},
\qquad
d=\frac{\lambda^2}{2(\lambda^2-1)},
\]
and define the Hilbert norm
\[
H(v)^2=cv_1^2+dv_2^2.
\]
Because \(\lambda>\sqrt2\), one has \(c>1>d>0\).

We first show
\[
H(v)\le N_\lambda(v)
\qquad(v\in\mathbb R^2).
\]
If \(F(v)\ge E(v)\), then
\[
v_2^2\le(\lambda^2-1)v_1^2,
\]
and therefore
\[
H(v)^2
\le
\left(c+d(\lambda^2-1)\right)v_1^2
=
\lambda^2v_1^2
=
F(v)^2.
\]
If \(E(v)\ge F(v)\), then
\[
v_2^2\ge(\lambda^2-1)v_1^2.
\]
Since
\[
c-1=\frac{\lambda^2-2}{2},
\qquad
d-1=-\frac{\lambda^2-2}{2(\lambda^2-1)},
\]
one obtains
\[
H(v)^2-E(v)^2
=
(c-1)v_1^2+(d-1)v_2^2
\le0.
\]
Thus \(H\le N_\lambda\) globally.

Next set
\[
C_\lambda
=
2\sqrt{1-\lambda^{-2}}.
\]
For a vector \(a\) whose active branch is Euclidean,
\[
N_\lambda(a)=E(a),
\]
the inequality \(H(a)^2\ge dE(a)^2\) gives
\[
E(a)\le\frac{H(a)}{\sqrt d}.
\]
For a vector \(b\) whose active branch is \(F\),
\[
N_\lambda(b)=F(b),
\]
the inequality \(H(b)^2\ge cb_1^2\) gives
\[
F(b)=\lambda|b_1|
\le
\frac{\lambda}{\sqrt c}H(b).
\]
Hence in either mixed active-branch case,
\[
E(a)F(b)
\le
\frac{\lambda}{\sqrt{cd}}H(a)H(b).
\]
But
\[
cd=\frac{\lambda^4}{4(\lambda^2-1)},
\]
so
\[
\frac{\lambda}{\sqrt{cd}}
=
2\sqrt{1-\lambda^{-2}}
=
C_\lambda.
\]

Now fix an admissible triple \(x,y,z\). There are four active-branch possibilities for
\[
N_\lambda(x-y)N_\lambda(z).
\]
If both factors use \(E\), Euclidean Ptolemy gives the required inequality with factor \(1\). If both use \(F\), the one-dimensional absolute-value metric gives the required inequality with factor \(1\). Since \(C_\lambda>1\), both cases are bounded by \(C_\lambda\) times the \(N_\lambda\)-denominator.

In either mixed case, the preceding estimate and Hilbert Ptolemy give
\[
N_\lambda(x-y)N_\lambda(z)
\le
C_\lambda H(x-y)H(z)
\]
\[
\le
C_\lambda\left(
H(x-z)H(y)+H(z-y)H(x)
\right)
\]
\[
\le
C_\lambda\left(
N_\lambda(x-z)N_\lambda(y)
+
N_\lambda(z-y)N_\lambda(x)
\right).
\]
Therefore
\[
C_{\mathrm{Pt}}(R_\lambda^2)
\le
2\sqrt{1-\lambda^{-2}}.
\]

For the reverse inequality put
\[
t_\lambda=\sqrt{\lambda^2-1},
\]
and take
\[
x=(1,t_\lambda),
\qquad
y=(1,-t_\lambda),
\qquad
z=(2,0).
\]
Then
\[
N_\lambda(x)=N_\lambda(y)=\lambda,
\]
and
\[
N_\lambda(x-z)=N_\lambda(z-y)=\lambda,
\]
because in all four vectors the Euclidean and \(F\)-branches tie. Also
\[
N_\lambda(x-y)=2t_\lambda,
\qquad
N_\lambda(z)=2\lambda.
\]
Thus the Ptolemy ratio is
\[
\frac{4\lambda t_\lambda}{2\lambda^2}
=
\frac{2\sqrt{\lambda^2-1}}{\lambda}
=
2\sqrt{1-\lambda^{-2}}.
\]
The upper and lower bounds coincide.

## Verification
The proof treats all four active-branch combinations in the numerator. The mixed cases are controlled by a single Hilbert norm chosen so that \(H\le N_\lambda\) on both branch regions and so that the mixed comparison factor is exactly the claimed constant.

The lower-bound triple is nonzero and pairwise distinct for every \(\lambda>\sqrt2\). Every denominator-side vector is exactly on the branch boundary
\[
E(v)=F(v),
\]
so no branch-choice approximation occurs.

As a consistency check,
\[
\lambda=2
\quad\Longrightarrow\quad
C_{\mathrm{Pt}}=\sqrt3.
\]
The proof is symbolic; no finite sampling, numerical optimization, or timeout is used.

## Relationship to prior work
Banaś and Frączek introduced the plane \(R_\lambda^2\) with exactly the norm above while studying deformation, convexity, and smoothness. Their Example 4.1 gives the same object but no Ptolemy calculation.

An earlier exact calculation covers the complementary interval \(1<\lambda\le\sqrt2\), where the value is \(\lambda\). The present claim starts strictly above that transition and supplies the missing second branch
\[
2\sqrt{1-\lambda^{-2}}.
\]

Zuo's 2012 paper gives general exactness criteria for Ptolemy constants of absolute normalized norms. Under the linear normalization
\[
(u,v)=(\lambda x_1,x_2),
\]
the present norm becomes
\[
M_\lambda(u,v)
=
\max\left\{
|u|,
\sqrt{u^2/\lambda^2+v^2}
\right\}.
\]
Its associated convex function is
\[
\psi_\lambda(t)
=
\max\left\{
1-t,
\sqrt{(1-t)^2/\lambda^2+t^2}
\right\},
\]
whose sharp Euclidean comparison occurs at an off-midpoint branch transition. Thus the midpoint extremality hypothesis in the relevant 2012 criterion does not imply this second-regime formula.

Zuo's 2018 comparison paper gives further exactness criteria for comparable absolute normalized norms. The inspected off-midpoint criteria require symmetry of the associated function about \(1/2\), while \(\psi_\lambda\) above is not symmetric for \(\lambda>1\). No Banaś--Frączek Ptolemy formula was located in the inspected 2018 material.

Yang and Yang's 2016 paper studies the generalized family
\[
\|x\|_{\lambda,p}
=
\max\{\lambda|x_1|,\|x\|_p\}
\]
and computes James-type and von Neumann--Jordan constants. Its \(p=2\) case is the present space, but those results concern different invariants and do not imply the Ptolemy formula.

## Limitations
The new quantified statement is restricted to \(\lambda>\sqrt2\); the first regime is not reproved as a new result. The argument is special to the max of one Euclidean norm and one coordinate seminorm, and no claim is made for the whole generalized \(p\)-family.

A 2015 article on additional sufficient conditions for Ptolemy constants of absolute normalized norms is a plausible bibliographic comparison source. Its metadata and abstract were accessible, but a verified full text was not obtained after bounded lawful retrieval attempts. This remains a residual originality risk rather than evidence of noncoverage.

An older equivalent computation under different affine or normalized-norm notation may also exist outside the checked indexes.

## References
1. J. Banaś and K. Frączek, “Deformation of Banach spaces,” *Commentationes Mathematicae Universitatis Carolinae* 34 (1993), 47--53. Stable record: DML-CZ 118554.
2. Z. Zuo, “The Ptolemy constant of absolute normalized norms on \(\mathbb R^2\),” *Journal of Inequalities and Applications* 2012, Article 107, DOI 10.1186/1029-242X-2012-107.
3. C. Yang and X. Yang, “On the James type constant and von Neumann-Jordan constant for a class of Banaś-Frączek type spaces,” *Journal of Mathematical Inequalities* 10 (2016), 551--558, DOI 10.7153/jmi-10-43.
4. Z.-F. Zuo, “On the Ptolemy constant of some concrete Banach spaces,” *Mathematical Inequalities & Applications* 21 (2018), 945--956, DOI 10.7153/mia-2018-21-64.
5. Z. Zuo, “A Reconsideration on the Ptolemy Constant of Absolute Normalized Norms,” *Acta Mathematica Sinica, Chinese Series* 58 (2015), 337--344, DOI 10.12386/A2015sxxb0033.
