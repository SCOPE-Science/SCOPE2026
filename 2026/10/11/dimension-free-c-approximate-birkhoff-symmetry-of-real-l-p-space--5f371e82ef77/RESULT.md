# Dimension-free \(C\)-approximate Birkhoff symmetry of real \(L_p\) spaces
## Finding
For any sigma-finite measure space \((\Omega,\Sigma,\mu)\) with \(\dim L_p(\mu)\ge2\), and any \(1<p<\infty\), the sharp global Chmieliński \(C\)-approximate symmetry constant is
\[
\boxed{
\chi_C(L_p(\mu))=
\max_{t>0}\Phi_p(t),\qquad
\Phi_p(t)=
\frac{t^{1/p}|t^{p-2}-1|}
{(1+t)^{1/p}(1+t^{p-1})^{(p-1)/p}}.
}
\tag{1}
\]
Its value is independent of dimension, atom structure, and measure weights. Every extremizer for \(p\ne2\) reduces to exactly two levels of the ratio \(y/x\), with opposite signs, on the support of \(x\). Conversely, two disjoint nonzero finite-measure sets always give equality pairs. In particular,
\[
\chi_C(\ell_p^n)=\chi_C(\ell_p^2),\qquad n\ge2,
\tag{2}
\]
and for \(q=p/(p-1)\),
\[
\chi_C(L_p(\mu))=\chi_C(L_q(\mu)).
\tag{3}
\]
The value is zero exactly for \(p=2\); otherwise it lies strictly between zero and one. The cubic Hölder pair has the closed form
\[
\chi_C(L_3(\mu))=\chi_C(L_{3/2}(\mu))
=\left(\frac{78\sqrt3-135}{16}\right)^{1/6}.
\tag{4}
\]

## Assumptions and scope
All Banach spaces and orthogonality relations are over the real scalars. The measure space is sigma-finite. Its \(L_p\) space has dimension at least two; equivalently, the measure algebra contains two disjoint measurable sets of strictly positive finite measure.

For \(x,y\in X\), Birkhoff--James orthogonality means
\[
x\perp_B y\quad\Longleftrightarrow\quad
\|x+\lambda y\|\ge\|x\|
\quad\text{for all real }\lambda.
\tag{5}
\]
Chmieliński approximate orthogonality is characterized by
\[
x\perp_B^\varepsilon y
\quad\Longleftrightarrow\quad
\exists f\in J(x):\ |f(y)|\le\varepsilon\|y\|,
\qquad 0\le\varepsilon<1.
\tag{6}
\]
Here \(J(x)\) is the collection of norm-one functionals taking value \(\|x\|\) at \(x\). Equation (6) is the real-space support-functional characterization from Chmieliński, Stypuła and Wójcik (2017), also recalled in Chmieliński, Khurana and Sain (2020).

The real space \(L_p(\mu)\) is smooth for \(1<p<\infty\); at a unit vector its unique support functional is
\[
J_p(x)=\operatorname{sgn}(x)|x|^{p-1}\in L_q(\mu),
\qquad q=\frac p{p-1}.
\tag{7}
\]
It follows that
\[
\chi_C(L_p(\mu))
=
\sup_{\substack{x,y\in S_{L_p(\mu)}\\
\int J_p(x)y\,d\mu=0}}
\left|\int J_p(y)x\,d\mu\right|.
\tag{8}
\]
The normalization to unit pairs is justified by homogeneity.

## Proof
### 1. An exact two-atom reduction when \(p>2\)
Fix unit vectors \(x,y\in L_p(\mu)\) with \(x\perp_B y\). Restrict attention to \(E=\{x\ne0\}\) and define the probability measure and measurable ratio
\[
d\nu=|x|^p\,d\mu\big|_E,
\qquad T=\frac yx\quad\text{on }E.
\tag{9}
\]
The orthogonality condition becomes
\[
\mathbb E_\nu T=0.
\tag{10}
\]
Moreover,
\[
\mathbb E_\nu|T|^p
=\int_E|y|^p\,d\mu\le1,
\tag{11}
\]
and the reverse support functional is
\[
\left|\int J_p(y)x\,d\mu\right|
=\big|\mathbb E_\nu\big(\operatorname{sgn}(T)|T|^{p-1}\big)\big|.
\tag{12}
\]
If \(T=0\) almost surely then (12) is zero. Otherwise (10) implies both signs occur. Write
\[
m=\mathbb E_\nu T_+=\mathbb E_\nu T_->0,
\qquad A=\mathbb E_\nu T_+^{p-1},
\qquad B=\mathbb E_\nu T_-^{p-1},
\tag{13}
\]
where \(T_+=\max(T,0)\) and \(T_-=\max(-T,0)\). Define positive numbers
\[
a=(A/m)^{1/(p-2)},\qquad
b=(B/m)^{1/(p-2)},\qquad
u_+=\frac ma,\qquad\nu_-=\frac mb.
\tag{14}
\]
The positive-moment inequalities obtained from Jensen, once with the conditional law on \(\{T>0\}\) and once with the size-biased law whose density is \(T_+/m\), give
\[
\nu_+\le\nu(T>0),
\qquad
\mathbb E_\nu T_+^p\ge m a^{p-1}.
\tag{15}
\]
Indeed, \(A\ge m^{p-1}/\nu(T>0)^{p-2}\) yields the first inequality. For the second,
\[
\frac{\mathbb E_\nu T_+^p}{m}
=\mathbb E_{\rm size} T^{p-1}
\ge\big(\mathbb E_{\rm size}T^{p-2}\big)^{(p-1)/(p-2)}
=a^{p-1}.
\tag{16}
\]
The negative sign yields the corresponding inequalities for \(\nu_-\) and \(b\). Hence
\[
S=\nu_++\nu_-\le1
\quad\text{and}\quad
\mathbb E_\nu|T|^p
\ge m(a^{p-1}+b^{p-1}).
\tag{17}
\]
Consider the three-valued law with probabilities \(\nu_+,\nu_-,1-S\) at the values \(a,-b,0\). Its first moment vanishes, its positive and negative moments of order \(p-1\) are exactly \(A,B\), and its moment of order \(p\) is no larger than (11). Deleting the zero atom and conditioning on the remaining two values produces the two-valued law
\[
\Pr(U=a)=\frac{b}{a+b},\qquad
\Pr(U=-b)=\frac{a}{a+b},
\tag{18}
\]
which has mean zero. The moment quotient satisfies
\[
\frac{|A-B|}{(\mathbb E_\nu|T|^p)^{(p-1)/p}}
\le
S^{1/p}
\frac{\left|\mathbb E\big(\operatorname{sgn}(U)|U|^{p-1}\big)\right|}
{(\mathbb E|U|^p)^{(p-1)/p}}
\le
\frac{\left|\mathbb E\big(\operatorname{sgn}(U)|U|^{p-1}\big)\right|}
{(\mathbb E|U|^p)^{(p-1)/p}}.
\tag{19}
\]
Using (11)--(12), every admissible reverse residual is at most the final two-point quotient. Direct substitution into (18) gives
\[
\frac{\left|\mathbb E\big(\operatorname{sgn}(U)|U|^{p-1}\big)\right|}
{(\mathbb E|U|^p)^{(p-1)/p}}
=
\frac{(ab)^{1/p}|a^{p-2}-b^{p-2}|}
{(a+b)^{1/p}(a^{p-1}+b^{p-1})^{(p-1)/p}}.
\tag{20}
\]
With \(t=a/b\), expression (20) is precisely \(\Phi_p(t)\), proving the upper bound in (1) for \(p>2\).

### 2. Sharpness on every admissible measure space
Choose disjoint measurable sets \(E,F\) with \(0<\mu(E),\mu(F)<\infty\), and define unit-norm indicators
\[
e=\frac{\mathbf1_E}{\mu(E)^{1/p}},
\qquad f=\frac{\mathbf1_F}{\mu(F)^{1/p}}.
\tag{21}
\]
For any \(a,b>0\), put \(w=b/(a+b)\) and
\[
x=w^{1/p}e+(1-w)^{1/p}f,
\quad
v=aw^{1/p}e-b(1-w)^{1/p}f,
\quad y=v/\|v\|_p.
\tag{22}
\]
Both \(x\) and \(y\) are unit vectors. Moreover,
\[
\int J_p(x)v\,d\mu
=aw-b(1-w)=0,
\tag{23}
\]
so \(x\perp_B y\). A direct computation shows that its reverse residual is the expression (20). It attains \(\Phi_p(a/b)\) for all ratios and attains the maximum once a maximizing ratio is selected. Continuity and the limits \(\Phi_p(t)\to0\) as \(t\downarrow0\) and \(t\to\infty\) ensure existence of a positive maximizing ratio whenever \(p\ne2\).

### 3. Rigidity of equality for \(p>2\)
For \(p>2\), the maximum is positive. If equality holds in (19), then \(S=1\), and equality must also hold in both strict Jensen inequalities (15)--(16) whenever the corresponding sign event has positive mass. Thus \(T\) is a positive constant on \(\{T>0\}\), a negative constant on \(\{T<0\}\), and never zero \(\nu\)-almost surely. Equality in (11) forces \(y=0\) almost everywhere on \(\{x=0\}\). Conversely any such two-level pair with a maximizing ratio and zero mean satisfies equality. The proof uses neither finiteness of \(\Omega\) nor any atomic assumption.

### 4. Hölder duality and \(1<p<2\)
Let \(1<p<\infty\), \(q=p/(p-1)\). For every unit pair \((x,y)\) in \(L_p(\mu)\), set
\[
X=J_p(y)\in S_{L_q},\qquad
Y=J_p(x)\in S_{L_q}.
\tag{24}
\]
The map \(J_p:S_{L_p}\to S_{L_q}\) is a bijection with inverse \(J_q\). It sends an ordered Birkhoff pair to another ordered Birkhoff pair in reversed order:
\[
\int J_p(x)y\,d\mu=0
\quad\Longleftrightarrow\quad
\int J_q(X)Y\,d\mu=0.
\tag{25}
\]
Their reverse residuals agree exactly:
\[
\left|\int J_p(y)x\,d\mu\right|
=
\left|\int J_q(Y)X\,d\mu\right|.
\tag{26}
\]
This proves (3) for every \(p\) in range, including infinite-dimensional spaces. In addition the scalar objectives obey the exact algebraic change-of-variables identity
\[
\Phi_p(t)=\Phi_q(t^{p-1}),
\qquad t>0,
\tag{26a}
\]
because \((t^{p-1})^{q-2}=t^{2-p}\), \(1/q=(p-1)/p\), and \((q-1)/q=1/p\). The map \(t\mapsto t^{p-1}\) is a bijection of \((0,\infty)\), so the scalar maxima for \(p\) and \(q\) agree. For \(1<p<2\), we have \(q>2\), so the preceding two-atom reduction applies in \(L_q\). The transformed two-level equality conditions again say that \(y/x\) assumes exactly one positive and one negative nonzero value, because the coordinatewise duality maps are invertible power maps. The explicit construction (22) remains valid. Thus (1) holds for the entire range.

### 5. Hilbert point and cubic special value
When \(p=2\), every orthogonal pair is symmetrically orthogonal and \(\Phi_2\equiv0\). When \(p\ne2\), the two-level construction gives a strictly positive value. No residual can equal one: equality in the \(L_p\)--\(L_q\) Hölder inequality would force \(J_p(y)=\pm J_p(x)\), hence \(y=\pm x\), contrary to \(x\perp_B y\) with unit vectors. Since a maximizing pair exists, the maximum is strictly less than one.

For \(p=3\), symmetry permits \(t\ge1\), and \(z=(t-1)/(t+1)\in[0,1)\) gives
\[
\Phi_3(t)^3=\frac{z^3(1-z^2)}{(1+z^2)^2}.
\tag{27}
\]
The derivative of the right-hand side is
\[
\frac{z^2(3-6z^2-z^4)}{(1+z^2)^3}.
\tag{28}
\]
It changes sign exactly once in \((0,1)\), at
\[
z^2=2\sqrt3-3.
\tag{29}
\]
Substitution yields
\[
\max\Phi_3(t)^6
=\frac{78\sqrt3-135}{16},
\tag{30}
\]
proving (4). Equation (3) transfers it to \(p=3/2\), as claimed.

## Verification
For reproducibility, install the single nonstandard checker dependency from `requirements.txt` and run `python verify.py`. The bundled standalone `verify.py` is a deterministic supplementary checker that:

- verifies symbolically the exact cubic variable substitution, derivative, and extremal algebraic expression (27)--(30);
- verifies the conjugate-exponent scalar identity on a reproducible collection of parameter values;
- checks the size-biased two-atom bound and equality for a deterministic family of rational finite distributions, including mass at zero and strongly unbalanced weights;
- constructs normalized finite-dimensional orthogonal pairs in several dimensions and tests the claimed dimension-free envelope.

Finite tests do not prove the global assertion or the equality classification. Those follow analytically from (15)--(26).

## Relationship to prior work
Chmieliński, Stypuła and Wójcik gave the support-functional characterization of Chmieliński approximate Birkhoff orthogonality. Chmieliński and Wójcik introduced its global symmetry property and an associated geometric constant. Chmieliński, Khurana and Sain developed local and global \(C\)-approximate symmetry and obtained qualitative results in polyhedral settings, including regular polygons.

Bose, Roy and Sain explicitly characterized the support functional, Birkhoff--James orthogonality, and exactly left/right symmetric points in sequence spaces \(\ell_p\), while Bose analyzed analogous qualitative properties in countable \(\ell_p\)-direct sums. These results do not state the sharp \(C\)-approximate **reverse residual** as a dimension-free \(L_p\) formula, and exact local symmetry classification does not imply the optimal global approximation parameter.

The main new mechanism is the exact size-biased reduction from an arbitrary measurable Birkhoff pair to a two-sign, two-valued pair without losing reverse residual. This extends the planar optimization to every real \(L_p\) space of dimension at least two, including nonatomic spaces, and characterizes all equality pairs. In particular the planar cubic value by itself does not imply (1)--(3) in higher dimensions.

## Limitations
The theorem concerns the real \(L_p\) scale for \(1<p<\infty\). It makes no assertion for \(p=1\), \(p=\infty\), complex scalars, vector-valued \(L_p\), or spaces without the specified measure assumptions. The formula in general is a one-variable maximum, not an elementary expression for every \(p\). It does not quantify the stability of approximate maximizers. The equality statement applies only when \(p\ne2\); at the Hilbert exponent all orthogonal pairs have zero reverse defect.

## References
1. J. Chmieliński, T. Stypuła and P. Wójcik, “Approximate orthogonality in normed spaces and its applications,” *Linear Algebra and its Applications* 531 (2017), 305--317, doi:10.1016/j.laa.2017.06.001, especially Theorem 2.3.
2. J. Chmieliński and P. Wójcik, “Approximate symmetry of Birkhoff orthogonality,” *Journal of Mathematical Analysis and Applications* 461 (2018), 625--640, doi:10.1016/j.jmaa.2018.01.031.
3. J. Chmieliński, D. Khurana and D. Sain, “Local approximate symmetry of Birkhoff--James orthogonality in normed linear spaces,” first public preprint arXiv:2012.08162v1, 15 December 2020, later *Results in Mathematics* 76 (2021), 136, doi:10.1007/s00025-021-01437-y; primary MSC 46B20.
4. B. Bose, S. Roy and D. Sain, “Birkhoff--James Orthogonality and Its Local Symmetry in Some Sequence Spaces,” first public preprint arXiv:2205.11586v1, 23 May 2022.
5. B. Bose, “Geometry of \(\ell_p\)-direct sums of normed linear spaces,” first public preprint arXiv:2309.14252v1, 25 September 2023; primary MSC 46B20.
