# Ternary quotients of four consecutive integers: exact Frobenius, genus and pseudo-Frobenius formulas

## Finding
For every integer \(x\ge3\), put \(r\in\{1,2\}\), \(a=3x-r\), and
\[
T_{x,r}=\{n\in\mathbb N_0:3n\in\langle a,a+1,a+2,a+3\rangle\}.
\]
The Frobenius number \(F\), genus \(g\), and full pseudo-Frobenius set are determined below. In particular,
\[
g(T_{x,1})=\frac{x(x-1)}2+\left\lfloor\frac{x+1}{3}\right\rfloor,
\qquad g(T_{x,2})=\frac{x(x-1)}2.
\]
The complete Frobenius-number formulas are

| Family | \(x\equiv0\pmod3\) | \(x\equiv1\pmod3\) | \(x\equiv2\pmod3\) |
|:---|:---|:---|:---|
| \(r=1\) | \(x^2-4x/3\) | \(x(x-2)+2(x-1)/3\) | \(x^2-x+\lfloor2x/3\rfloor\) |
| \(r=2\) | \(x^2-5x/3\) | \(x(x-2)+(x-1)/3\) | \(x^2-x-\lfloor2x/3\rfloor\) |

For the complete pseudo-Frobenius set, define \(q_0=x-1\) if \(x\equiv1\pmod3\) and \(q_0=x\) otherwise, and set
\[
A=\left\lfloor\frac{rq_0}{3}\right\rfloor,\qquad B=x-1-A,\qquad
q(t)=\begin{cases}
\lceil-3t/r\rceil,&t<0,\\
\lceil3t/(3-r)\rceil,&t\ge0,
\end{cases}\qquad w(t)=xq(t)+t.
\]
Let \(M_{x,r}\) be the following set of *integer offsets*:

| Family | \(x\equiv0\pmod3\) | \(x\equiv1\pmod3\) | \(x\equiv2\pmod3\) |
|:---|:---|:---|:---|
| \(r=1\) | \(\{-A,B\}\) | \(\{-A,B-1,B\}\) | \(\{B\}\) |
| \(r=2\) | \(\{-A,-A+1\}\cup(\{B\}\text{ if }B>0)\) | \(\{-A,-A+1,B\}\) | \(\{-A,B\}\) |

Then
\[
\operatorname{PF}(T_{x,r})=\{w(t)-x:t\in M_{x,r}\}.
\]
In particular the types (cardinalities of these sets), in the same order of congruence classes \(0,1,2\pmod3\), are \((2,3,1)\) for \(r=1\) and \((3,3,2)\) for \(r=2\), **except** that the type is \(2\) for \((r,x)=(2,3)\).

## Assumptions and scope
The semigroup \(\langle A\rangle\) means all nonnegative integer combinations of the elements of \(A\). Its genus is the number of excluded nonnegative integers, its Frobenius number the largest excluded integer, and its pseudo-Frobenius set consists of excluded integers \(f\) such that \(f+s\) lies in the semigroup for every positive semigroup element \(s\). The families require \(x\ge3\) and \(r=1\) or \(2\), so \(a\ge7\) and \(3\nmid a\). All quantifiers in the formulas above range over these integer parameters. The theorem does not address \(3\mid a\), other quotient denominators, or longer generating intervals.

## Proof
**1. Interval reduction.** For each \(h\ge0\), the sums of exactly \(h\) generators from \(\{a,a+1,a+2,a+3\}\) form *every* integer of \([ah,(a+3)h]\). Thus a quotient element obtained using \(h\) generators lies in the integer interval
\[
I_h=\left[hx-\left\lfloor\frac{rh}{3}\right\rfloor,\;hx+\left\lfloor\frac{(3-r)h}{3}\right\rfloor\right].
\]
Write \(J_h=I_h-hx\). The endpoints of \(J_h\) move monotonically outwards as \(h\) increases. Its cardinality is \(h+1\) when \(3\mid h\) and \(h\) otherwise.

**2. An exact Apéry staircase.** Define \(q_0,A,B,q(t)\) as above. The interval \([-A,B]\) contains exactly \(x\) integers and represents every residue class modulo \(x\) once. If \(x\equiv0\pmod3\), the full \(J_{q_0}\) has one extra right endpoint congruent modulo \(x\) to its left endpoint; discarding the right endpoint chooses the smaller represented integer. In the other two congruence classes the full \(J_{q_0}\) contains exactly \(x\) integers. For each integer \(t\) in this chosen interval, \(q(t)\) is precisely the smallest \(h\) for which \(t\in J_h\).

No other representation gives a smaller element of that residue class: prior to \(q_0\), the nested \(J_h\) have fewer than \(x\) offsets and cannot contain a different representative of the same residue; at \(q_0\) only the stated duplicated endpoint can occur. For later \(h\), the lower endpoint of \(I_{q_0+1}\) is at least the upper endpoint of \(I_{q_0}\), by direct substitution of \(x\bmod3\) into
\[
\min I_{q_0+1}-\max I_{q_0}
=x-\left\lfloor\frac{r(q_0+1)}3\right\rfloor
 -\left\lfloor\frac{(3-r)q_0}3\right\rfloor\ge0.
\]
The later lower endpoints are strictly increasing. Therefore
\[
\operatorname{Ap}(T_{x,r};x)=\{w(t)=xq(t)+t:-A\le t\le B\}.
\]
This also shows that \(x\) is the multiplicity.

**3. Explicit generators.** For \(r=1\), the negative offsets and positive even/odd offsets obey
\[
w(-j)=j(3x-1),\quad w(2j)=j(3x+2),\quad
w(2j+1)=j(3x+2)+(2x+1).
\]
For \(r=2\), they obey
\[
w(-2j)=j(3x-2),\quad w(-(2j+1))=j(3x-2)+(2x-1),\quad
w(j)=j(3x+1).
\]
Consequently, since every semigroup element is an Apéry element plus a nonnegative multiple of \(x\),
\[
T_{x,1}=\langle x,2x+1,3x-1,3x+2\rangle,
\qquad T_{x,2}=\langle x,2x-1,3x-2,3x+1\rangle.
\]
Some displayed generators can be redundant at the smallest parameter values; their use remains valid.

**4. Genus and Frobenius number.** The classical Apéry identities give
\[
F=\max_{-A\le t\le B}w(t)-x,\qquad
 g=\frac1x\sum_{t=-A}^{B}w(t)-\frac{x-1}{2}
 =\sum_{t=-A}^{B}q(t)-A.
\]
Substituting the two branches of \(q(t)\) and summing the linear and alternating-ceiling terms gives the genus formulas. On each branch \(w(t)\) is monotone with absolute offset, so the maximum is at \(-A\) or \(B\). Evaluating these two possibilities for \(x\equiv0,1,2\pmod3\) yields the Frobenius table displayed above.

**5. The pseudo-Frobenius set.** An Apéry element \(w(t)\) is maximal under the order \(u\preceq v\iff v-u\in T_{x,r}\) precisely if none of the three displayed generators other than \(x\) can be added to it while remaining in the Apéry set. To check this without an implicit search, for a generator \(g=cx+d\) let \(t'\) be the unique integer in \([-A,B]\) congruent to \(t+d\pmod x\). Then
\[
w(t)+g=w(t')\quad\Longleftrightarrow\quad
q(t')-q(t)=c+\frac{t+d-t'}{x}.
\]
This equation involves only the above explicit ceiling functions. On the \(r=1\) negative branch, addition by \(3x-1\) connects consecutive negative offsets; on its positive branch, addition by \(3x+2\) connects offsets differing by two, and addition by \(2x+1\) connects each nonterminal even offset to the next odd offset. Thus only \(-A,B-1,B\) may remain, and \(B-1\) is eliminated when \(B\) is odd. The cross-branch equality at the remaining negative endpoint occurs exactly for \(x\equiv2\pmod3\): \(w(-A)+(3x-1)=w(B)\). In the other cases the displayed equality criterion excludes further cross-branch edges.

On the \(r=2\) negative branch, addition by \(3x-2\) connects offsets two steps apart and addition by \(2x-1\) connects each nonterminal even absolute offset to the next odd one; addition by \(3x+1\) connects successive positive offsets. Thus the only possible maximal offsets are \(-A,-A+1,B\). The explicit equality criterion excludes all cross-branch eliminations here. When \(A\) is odd, \(-A+1\) is already eliminated by the negative-branch \(2x-1\) edge; when \(B=0\), zero cannot be maximal. Substitution of \(x\bmod3\) gives exactly the table for \(M_{x,r}\). The standard correspondence \(\operatorname{PF}(T)=\{w-x:w\text{ maximal in }\operatorname{Ap}(T;x)\}\) completes the proof.

## Verification
Running `python3 verify.py` reproduces two types of finite checks. Exact integer Apéry / maximality / genus / Frobenius comparisons pass for both families for every \(3\le x\le800\) (1596 parameter pairs). Separate direct interval-membership and gap/pseudo-Frobenius enumeration passes for \(3\le x\le90\) (176 parameter pairs). The direct membership test uses the inequality \(\lceil3n/(a+3)\rceil\le\lfloor3n/a\rfloor\), not the Apéry construction. These computations supplement, but do not prove, the infinite formulas.

## Relationship to prior work
Adeniran, Butler, Defant, Gao, Harris, Hettle, Liang, Nam and Volk (arXiv:1809.09360, §3) explicitly posed the Frobenius/genus problem for quotients of arithmetic-progression numerical semigroups with three or more steps and unrestricted quotient denominators. Liu (arXiv:2312.06096, §1–3) treated the case in which the quotient denominator divides the first generator, whereas \(3\nmid a\) here. Liu's later generator theorem (arXiv:2312.10889, §3) can produce a generally nonminimal generating set for arbitrary quotients, but it does not give the present parameter-uniform Apéry, Frobenius, genus or pseudo-Frobenius formulas. Liu's arXiv:2604.26415 studies quotients of a different GCNS generator family and also assumes the denominator divides its first generator. The general Apéry/Frobenius identities and quotient definitions are established background, not new claims here.

## Limitations
The main theorem is specific to the ternary quotient of four consecutive generators with the smallest generator prime to three. The first family has a periodic type pattern while the second has one small exceptional parameter. It does not settle the full unrestricted arithmetic-progression quotient problem. Priority can be affected by unindexed specializations of general semigroup results, especially the generator construction of arXiv:2312.10889; the statement is offered with that residual risk.

## References
1. A. Adeniran et al., *On the genus of a quotient of a numerical semigroup*, arXiv:1809.09360, first posted 2018-09-25, §3 and its concluding problem.
2. F. Liu, *On quotients of numerical semigroups for almost arithmetic progressions*, arXiv:2312.06096, first posted 2023-12-11, §1–3.
3. F. Liu, *Generating functions for the quotients of numerical semigroups*, arXiv:2312.10889, first posted 2023-12-18, §2.2–3.
4. F. Liu, *The Frobenius problem for a class of quotients of numerical semigroups*, arXiv:2604.26415, first posted 2026-04-29, §1–3.
