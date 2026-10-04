# Blackburn optimality for length-six non-overlapping codes from alphabet size ten
## Finding
For every integer \(q\ge 10\), let \(S(q,6)\) denote the maximum size of a \(q\)-ary non-overlapping code of length six. Then \[S(q,6)=\max_{1\le \ell\le q-1}\ell^5(q-\ell).\] Consequently Blackburn\'s construction with \(k=5\) and \(S=I^5\) is maximum for every \(q\ge10\), proving the length-six case of Blackburn\'s eventual-optimality conjecture with an explicit tail beginning at ten.

Equivalently, writing \(c=q-\ell\), the maximum is \(\max_{{1\le c\le q-1}} c(q-c)^5\). The lower bound is the one-boundary code obtained from a partition of the alphabet into sets of sizes \(q-c\) and \(c\).

## Assumptions and scope
A length-six code \(C\subseteq\Sigma^6\) is non-overlapping when no nonempty proper prefix of any codeword is a suffix of any codeword, including itself. The alphabet has \(|\Sigma|=q\), with integer \(q\ge10\). The quantity \(S(q,6)\) is the largest possible cardinality of such a code.

The proof uses the exact SQN formulation of Stanovnik, Moškon and Mraz: for nonnegative integers \(x_i,y_i\),
\[
S(q,6)=\max\sum_{{i=1}}^5 x_i y_{{6-i}},
\]
subject to \(x_1+y_1=q\), \(x_1,y_1>0\), and
\[
x_i+y_i=\sum_{{j=1}}^{{i-1}}x_jy_{{i-j}}\qquad(2\le i\le5).
\]
Their theorem identifies this integer program with the true maximum over all non-overlapping codes, so no structural subclass is being assumed.

## Proof
By the symmetry \((x,y)\leftrightarrow(y,x)\), assume \(a=x_1\le b=y_1\), so \(a+b=q\). Put
\[
u=x_2,\qquad y_2=ab-u,
\]
\[
T_3=a^2b+(b-a)u,\qquad v=x_3,\qquad y_3=T_3-v,
\]
and
\[
T_4=a y_3+u y_2+vb,\qquad w=x_4,\qquad y_4=T_4-w.
\]
At level five, if \(x_5+y_5=T_5\), then the contribution involving \(x_5,y_5\) is \(a y_5+b x_5\). Since \(a\le b\), it is maximized by \(x_5=T_5\), \(y_5=0\). After this substitution, the SQN objective is
\[
F=a^4b^2+3a^2b^2u-a^2u^2+2ab^2v-2auv+b^2u^2+(b^2-2u)w-u^3-v^2.
\]
Thus, for fixed \(u,v\), the maximizing fourth-level choice is \(w=T_4\) when \(2u\le b^2\), and \(w=0\) when \(2u\ge b^2\).

First suppose \(2u\le b^2\). For fixed \(u\), after taking \(w=T_4\), the objective is a concave quadratic in \(v\). If its vertex lies at or beyond the feasible endpoint \(v=T_3\), the maximum is attained at \(v=T_3\). At that endpoint the objective is
\[
H(u)=a^2b^3(q+a)+b^2(b-a)(b+3a)u-3b^2u^2+u^3.
\]
Write \(x=a/b\) and \(z=u/b^2\). Then
\[
\frac{{H(u)}}{{q^6}}=G(x,z):=\frac{{x^2(1+2x)+(1-x)(1+3x)z-3z^2+z^3}}{{(1+x)^6}}.
\]
If \(x\le1/4\), the derivative of the numerator with respect to \(z\) is decreasing on \(0\le z\le x\) and at \(z=x\) equals \(1-4x\ge0\). Hence \(H\) is maximized at \(z=x\), giving \(H=ab^5\).

Now assume \(x\ge1/4\). The unique maximizing \(z=z_*(x)\in[0,x]\) satisfies
\[
3z^2-6z+(1-x)(1+3x)=0.
\]
This root obeys \(z_*<13/50\): at \(z=13/50\) the left side is
\[
-\frac{{7500x^2-5000x+893}}{{2500}}<0,
\]
because the numerator has discriminant \(-1790000\). Along the stationary curve, differentiating \(G\) gives a numerator equal to \(-2B\), where
\[
B=3x^3-3x^2z-4x^2+6xz+x-5z+1.
\]
The coefficient of \(z\) in \(B\) is \(-3x^2+6x-5<0\). Therefore
\[
B\ge \frac{{150x^3-239x^2+128x-15}}{{50}}.
\]
The cubic on the right is strictly increasing: its derivative is \(2(225x^2-239x+64)\), whose discriminant is \(-479\); at \(x=1/4\) the cubic equals \(141/32\). Hence \(B>0\), so \(G(x,z_*(x))\) strictly decreases for \(x\ge1/4\). Its value at \(x=1/4\) is
\[
K:=\frac15\left(\frac45\right)^5=\frac{{1024}}{{15625}}.
\]
Thus this endpoint branch is at most \(Kq^6\) whenever \(a/b\ge1/4\).

It remains to check the case where the concave quadratic in \(v\) has an interior vertex. In scaled variables its vertex can be feasible only when \(x\ge1/3\), and then only for
\[
z\ge z_0:=\frac{{(1-x)(1+2x)}}{{2(2-x)}}.
\]
The value at the vertex, as a function of \(z\), has derivative that is a convex quadratic in \(z\). At \(z=z_0\) this derivative is
\[
\frac{{5(x-1)(4x^2-x+1)}}{{4(x-2)^2}}\le0.
\]
At the other endpoint it is \(-3x^2+3x-1<0\) when \(1/3\le x\le1/2\), and it is
\[
-\frac{{8x^3-12x^2+12x-3}}4<0
\]
when \(1/2\le x\le1\); the cubic in the numerator is increasing there and equals \(1\) at \(x=1/2\). Convexity therefore makes the derivative nonpositive throughout the feasible interval. The interior-vertex value is consequently no larger than its value at \(z=z_0\), where the vertex meets \(v=T_3\); this is already bounded by the preceding \(H\)-analysis.

Finally suppose \(2u\ge b^2\). This can occur only for \(x=a/b\ge1/2\). The maximizing quadratic vertex in \(v\) is feasible and, with \(z=u/b^2\), gives
\[
\frac{F}{q^6}=\frac{{x^4+x^2+x^2z+z^2-z^3}}{{(1+x)^6}},\qquad \frac12\le z\le x\le1.
\]
Since \(x^2z\le x^2\) and \(z^2(1-z)\le4/27\), the numerator is at most \(x^4+2x^2+4/27\). For \(x\ge1/2\),
\[
x^4+2x^2+\frac4{{27}}\le\frac{{(1+x)^6}}{{16}}.
\]
After multiplying by \(432\), the difference is
\[
R(x)=27x^6+162x^5-27x^4+540x^3-459x^2+162x-37.
\]
Here \(R(1/2)=35/64>0\), and
\[
R'(x)=54\left[x^3(3x^2+15x-2)+(30x^2-17x+3)\right]>0
\]
for \(x\ge1/2\). Therefore this branch is at most \(q^6/16<Kq^6\).

We have proved: if \(a\le q/5\), every feasible solution has value at most \(ab^5\); if \(a\ge q/5\), every feasible solution has value at most \(Kq^6\).

For integer \(q\ge10\), let \(c=\lfloor q/5\rfloor\) and \(t=c/q\). Then \(1/7\le t\le1/5\). The function \(h(t)=t(1-t)^5\) increases up to \(t=1/6\) and decreases afterwards, while
\[
h(1/7)>h(1/5)=K.
\]
Hence \(c(q-c)^5\ge Kq^6\). Therefore every SQN solution is bounded above by
\[
M(q):=\max_{{1\le c\le q-1}}c(q-c)^5=\max_{{1\le\ell\le q-1}}\ell^5(q-\ell).
\]
Blackburn's \(k=5\) construction with \(|I|=\ell\), \(|J|=q-\ell\), and \(S=I^5\) has exactly \(\ell^5(q-\ell)\) codewords, so it attains \(M(q)\). This proves the formula.

## Verification
`verify.py` uses exact integer and rational arithmetic only. It independently expands the SQN recurrence into the displayed objective on an integer test box, checks every discriminant and endpoint constant used in the universal inequalities, compares the reduced optimizer with direct exhaustive SQN enumeration for \(2\le q\le5\), reproduces the known small-alphabet values through \(q=9\), and checks the theorem by exact reduced SQN optimization for every \(10\le q\le80\). It returns:

`VERIFY_OK theorem_q_min=10 scan_q_max=80 q9_exception=33872 blackburn_q9=33614`

The finite scans are stress tests only. The statement for all \(q\ge10\) follows from the symbolic inequalities above.

## Relationship to prior work
Blackburn introduced the construction used for the lower bound and conjectured that for every fixed length, sufficiently large alphabets have a maximum code of the \(k=n-1\) form. His paper proves exact maxima only through length three and proves optimality of this construction when the code length divides the alphabet size.

Stanovnik, Moškon and Mraz later proved the SQN characterization used here. Their published exact computations cover \(3\le q\le6\) for lengths through sixteen, and they explicitly state that no simple formula is known for larger codeword lengths; they also state that Blackburn's conjecture remained unresolved. The present theorem supplies a closed exact formula for the full infinite tail \(q\ge10\) at length six.

## Limitations
The theorem determines the maximum size, not the number or isomorphism types of maximum codes. It does not settle lengths \(n\ge7\), nor does it claim that every maximum length-six code is itself a Blackburn code. The proof depends on the published SQN equivalence between maximum non-overlapping codes and its integer optimization formulation. Non-indexed or unpublished duplicate work remains a residual originality risk.

## References
1. S. R. Blackburn, “Non-overlapping codes,” arXiv:1303.1026, first public version 5 March 2013; later IEEE Transactions on Information Theory 61 (2015), 4890–4894.
2. L. Stanovnik, M. Moškon, and M. Mraz, “In search of maximum non-overlapping codes,” Designs, Codes and Cryptography 92 (2024), 1299–1326, DOI: 10.1007/s10623-023-01344-z.
