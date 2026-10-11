# Review of Three-regime boundary defect of weighted Bergman kernel norms

## Correctness

PASS. With
\[
\beta=\alpha+2,
\qquad
c=(p-1)\beta,
\qquad
a=(\beta+c)/2,
\qquad
d=(\beta-c)/2,
\]
direct integration gives
\[
\|K_z\|_{p,\alpha}^p
=
{}_2F_1(a,a;\beta;|z|^2).
\]
Euler's transformation therefore gives the exact normalized profile
\[
(1-|z|^2)^c\|K_z\|_{p,\alpha}^p
=
{}_2F_1(d,d;\beta;|z|^2).
\]

Gauss' formula yields the boundary constant. If
\[
c>1,
\]
the transformed hypergeometric function has a finite derivative at the boundary, whose exact value gives the linear term. If
\[
0<c<1,
\]
the connection formula shows that the nonanalytic branch
\[
(1-|z|^2)^c
\]
dominates the ordinary linear term. At
\[
c=1,
\]
the derivative becomes zero-balanced and grows logarithmically, producing the
\[
s\log(1/s)
\]
term after integration. Taking the positive
\[
p
\]
th root gives the stated coefficients. The case
\[
p=2
\]
reduces identically to
\[
{}_2F_1(0,0;\beta;x)=1.
\]

## Originality

PASS. The recent lead source gives the two-sided kernel norm estimate and uses normalized kernels in its compactness theorem. The earlier sharp Forelli--Rudin paper gives the exact leading constant through a sharp global bound and its boundary behavior. Neither inspected source states the first normalized boundary defect or the transition in that defect at
\[
(p-1)(\alpha+2)=1.
\]

Targeted searches included the lead source identifier, the exact weighted-kernel normalization, second-order Forelli--Rudin terminology, hypergeometric boundary corrections, and the critical relation. The closest published-finding results concern unrelated endpoint kernel norms or other logarithmic phase transitions and do not imply this weighted Bergman statement.

## Value

PASS. The recent operator theorem uses normalized weighted Bergman kernels as its test family for weak convergence and the Berezin-transform compactness criterion. Its Lemma 8 leaves a finite gap between the elementary lower normalization and the sharp upper constant.

The new result resolves the boundary approach at the first nontrivial order and shows that the regularity of that normalization changes qualitatively across a natural exponent curve. The critical logarithm is not visible in the source inequalities or in the leading sharp Forelli--Rudin constant. This is a structural fact about the exact kernel test family rather than a numerical refinement of an arbitrary parameter slice.

Same-model review: passed. Independent audit: not yet performed.
