# Exact size and enumeration of maximum length-five non-overlapping codes

A **non-overlapping code** (also called a cross-bifix-free, mutually uncorrelated, or strong comma-free code) is a set \(C\subseteq\Sigma^n\) such that no nonempty proper prefix of a codeword is a suffix of any codeword, including the same codeword. Let \(S(q,n)\) be the maximum cardinality of such a code over an alphabet of size \(q\), and let \(N(q,n)\) be the number of maximum codes on a fixed labeled alphabet.

## Theorem

For length five,

\[
S(2,5)=2,\qquad S(3,5)=17,
\]

and for every \(q\ge4\),

\[
\boxed{\;S(q,5)=\max_{1\le \ell\le q-1}\ell^4(q-\ell).\;}
\]

The maximizing integer \(\ell=\ell_q\) is unique. More explicitly, if \(q=5m+r\), then

\[
\ell_q=\begin{cases}
4m,&r=0,\\
4m+1,&r=1,\\
4m+2,&r=2,\\
4m+2,&r=3,\\
4m+3,&r=4.
\end{cases}
\]

Consequently, for \(q\ge4\) every maximum code is, up to exchanging prefixes and suffixes, a Blackburn \(k=4\) code

\[
I^4J=\{x_1x_2x_3x_4y:x_i\in I,\ y\in J\},
\]

where \(\Sigma=I\sqcup J\), \(|I|=\ell_q\), and \(|J|=q-\ell_q\). The number of maximum codes is

\[
N(2,5)=8,\qquad N(3,5)=12,
\]

and, for \(q\ge4\),

\[
\boxed{\;N(q,5)=2\binom q{\ell_q}.\;}
\]

In particular, the previously computed values

\[
(S(q,5))_{q=2}^6=(2,17,81,256,625)
\]

and

\[
(N(q,5))_{q=2}^6=(8,12,8,10,12)
\]

are recovered exactly.

## Context

Blackburn proved exact formulas for lengths two and three and conjectured that, for each fixed \(n>2\) and all sufficiently large alphabet sizes, a maximum non-overlapping code is obtained from his construction with \(k=n-1\). Stanovnik, Moškon and Mraz later characterized maximal non-overlapping codes, reduced the exact maximum problem to the integer program SQN\((q,n)\), proved an exact formula for length four, and reported that no simple formula was then available for larger lengths. Their computation gives the length-five values above for \(2\le q\le6\), and specifically shows the exceptional ternary value \(S(3,5)=17\), which is larger than the best \(k=4\) Blackburn value \(16\).

The theorem here solves SQN\((q,5)\) symbolically for every alphabet size. Thus Blackburn's proposed \(k=n-1\) pattern is optimal for **all \(q\ge4\) when \(n=5\)**, with \(q=3\) as a genuine small-alphabet exception.

## Proof

Stanovnik, Moškon and Mraz show that the exact maximum is the optimum of

\[
S(q,n)=\max\sum_{i=1}^{n-1}x_i y_{n-i},
\]

subject to

\[
x_1+y_1=q,\qquad
x_i+y_i=\sum_{j=1}^{i-1}x_jy_{i-j}\quad(i>1),
\]

with \(x_1,y_1>0\) and all variables nonnegative integers. We solve this program for \(n=5\).

By the symmetry \((x,y)\leftrightarrow(y,x)\), assume

\[
a:=x_1\ge b:=y_1,\qquad a+b=q.
\]

Put

\[
u=x_2,\qquad v=y_2=ab-u,
\]

and

\[
w=x_3,\qquad z=y_3=M-w,
\]

where

\[
M=av+bu=a^2b-(a-b)u.
\]

Finally let

\[
N=x_4+y_4=az+uv+bw.
\]

The objective is

\[
T=ay_4+uz+wv+bx_4.
\]

For fixed earlier variables, this is affine in \(x_4\) with coefficient \(b-a\le0\), so an optimum may be taken with \(x_4=0\). Substitution gives

\[
T=(a^2+u)M+auv+cw,
\qquad
c=2ab-a^2-2u.
\]

Because \(0\le w\le M\), the sign of \(c\) determines the optimal endpoint.

### 1. The branch \(c\le0\)

Here \(w=0\), and

\[
T_0(u)=a^4b+a^2(3b-a)u+(b-2a)u^2.
\]

This is a concave quadratic.

If \(a\ge3b\), then its linear coefficient is nonpositive, hence

\[
T\le T_0(0)=a^4b.
\]

Equality forces \(u=0\), and then \(w=x_4=0\). This is exactly the \(I^4J\) size pattern.

Now suppose \(b\le a<3b\). Its unrestricted vertex is

\[
u_*=
\frac{a^2(3b-a)}{2(2a-b)},
\]

which lies in \([0,ab]\) and also lies in the allowed half-line \(c\le0\). Therefore

\[
T\le T_0(u_*)
=
\frac{a^4(a^2+2ab+5b^2)}{4(2a-b)}.
\]

Writing \(t=a/b\in[1,3)\), the inequality

\[
T_0(u_*)<\frac{81}{1024}(a+b)^5
\]

is equivalent to

\[
81(2t-1)(t+1)^5-256t^4(t^2+2t+5)>0.
\]

The left side factors as

\[
(3-t)P(t),
\]

where

\[
P(t)=94t^5+65t^4+260t^3-30t^2-90t-27.
\]

Now \(P(1)=272\), and

\[
P'(t)=470t^4+260t^3+780t^2-60t-90>0
\qquad(t\ge1),
\]

so \(P(t)>0\) on \([1,3]\). This proves the strict bound.

### 2. The branch \(c\ge0\)

Here \(w=M\), and simplification gives

\[
T_1(u)=b\bigl(2a^3b-2a^2u+2abu-u^2\bigr).
\]

Its derivative with respect to \(u\) is

\[
-2b\bigl(a(a-b)+u\bigr)\le0,
\]

so

\[
T\le T_1(0)=2a^3b^2.
\]

Moreover \(c\ge0\) implies \(a\le2b\). Even without this restriction, maximizing \(2a^3b^2\) subject to \(a+b=q\) gives

\[
T\le\frac{216}{3125}q^5
<\frac{81}{1024}q^5.
\]

Thus every solution with \(a<3b\) is strictly below \(81q^5/1024\).

### 3. Comparing with the Blackburn construction

Let

\[
M_q:=\max_{1\le \ell\le q-1}\ell^4(q-\ell).
\]

For all \(q\ge4\), except temporarily \(q=7\), we have

\[
M_q\ge\frac{81}{1024}q^5.
\]

Indeed, write \(q=4m+r\), \(0\le r\le3\), and choose

\[
b=m=\left\lfloor\frac q4\right\rfloor,
\qquad a=q-m.
\]

For \(r=0\) equality holds. For \(r=1,2,3\), after multiplying by \(1024\), the differences \(1024a^4b-81q^5\) are respectively

\[
6912m^4+3456m^3-672m^2-596m-81,
\]

\[
32(432m^4+432m^3-168m^2-298m-81),
\]

and

\[
81(256m^4+384m^3-224m^2-596m-243).
\]

The first two are positive for \(m\ge1\); the third is positive for \(m\ge2\). The only uncovered value with \(q\ge4\) is therefore \(q=7\).

Combining the preceding bounds, for \(q\ne7\):

- if \(a<3b\), then \(T<81q^5/1024\le M_q\);
- if \(a\ge3b\), then \(T\le a^4b\le M_q\), with equality only when \(u=w=x_4=0\).

Hence \(S(q,5)=M_q\), and every optimum has the Blackburn \(k=4\) pattern.

For \(q=7\), after symmetry the possibilities are \((a,b)=(4,3),(5,2),(6,1)\). The first two satisfy the upper bounds

\[
T\le1152<1296,
\qquad
T\le\frac{40625}{32}<1296,
\]

respectively, while \((6,1)\) gives \(T\le6^4=1296\), achieved at \(u=w=x_4=0\). Thus the same conclusion holds for \(q=7\).

### 4. The two small alphabets

For \(q=3\), symmetry gives \((a,b)=(2,1)\). Then \(u\in\{0,1,2\}\), \(c=-2u\le0\), and

\[
T=16+4u-3u^2.
\]

The unique maximum is \(17\) at \(u=1\). The corresponding size pattern is

\[
(x_1,x_2,x_3,x_4)=(2,1,0,0),
\qquad
(y_1,y_2,y_3,y_4)=(1,1,3,7).
\]

For example, over \(\{0,1,2\}\), take

\[
L_1=\{0,1\},\ R_1=\{2\},\quad
L_2=\{02\},\ R_2=\{12\},\quad
L_3=L_4=\varnothing,
\]

with later \(R_i\) forced by the partition construction. This gives a 17-word non-overlapping code.

For \(q=2\), \(a=b=1\) and \(u\in\{0,1\}\). Both possibilities give \(T=2\), so \(S(2,5)=2\).

### 5. The maximizing split and enumeration of maximum codes

The real function \(f(x)=x^4(q-x)\) increases up to \(4q/5\) and decreases afterward, so its maximizing integer is one of the two nearest integers to \(4q/5\). Writing \(q=5m+r\), the only comparison needed in each nonzero residue class is between those adjacent candidates. The difference “upper candidate minus lower candidate” is

\[
\begin{array}{c|c}
r & f(\lceil 4q/5\rceil)-f(\lfloor 4q/5\rfloor)\\
\hline
1 & m(96m^2+16m+1),\\
2 & 32m^3+16m^2-m-1,\\
3 & -32m^3-80m^2-63m-16,\\
4 & -(m+1)(96m^2+176m+81).
\end{array}
\]

For the relevant ranges \(q\ge4\), these quantities are respectively positive, positive, negative and negative. Thus the maximizing integer is unique and equals

\[
\ell_q=\begin{cases}
4m,&q=5m,\\
4m+1,&q=5m+1,\\
4m+2,&q=5m+2,\\
4m+2,&q=5m+3,\\
4m+3,&q=5m+4.
\end{cases}
\]

For \(q\ge4\), the equality analysis above shows that, after fixing which side has size \(\ell_q\), all later partitions are forced. There are \(\binom q{\ell_q}\) choices of the large alphabet part and two orientations, so

\[
N(q,5)=2\binom q{\ell_q}.
\]

For \(q=3\), there are three choices for the two-symbol first part, two choices for the one-element set \(L_2\subset L_1R_1\), and two orientations, giving \(N(3,5)=12\). For \(q=2\), the two choices of the first singleton partition combine with four optimal higher-level size patterns, giving \(N(2,5)=8\).

## Verification

`artifacts/verify_length5.py` independently enumerates the finite SQN\((q,5)\) variables for \(2\le q\le12\), checks the theorem's closed form, verifies that every normalized optimum for \(4\le q\le12\) has the Blackburn \(k=4\) size pattern, checks the known \(q\le6\) size values from the 2024 table, and directly tests all prefix-suffix overlaps in the explicit ternary 17-word construction. It additionally performs full optimizer enumeration for \(2\le q\le7\) and applies Proposition 11 to recover the known counts \(N(q,5)\) for \(q\le6\) and the theorem's count for \(q=7\). The deterministic output is recorded in `artifacts/verification_output.txt`.

## Originality and scope

The 2024 exact-optimization paper explicitly states that no simple formula was then available beyond length four and gives only computed instances for length at least five. Searches through the present using the equivalent terms *non-overlapping*, *cross-bifix-free*, *mutually uncorrelated*, and *strong comma-free* found later work on variable-length codes, balance/run-length constraints, restricted overlap lengths, and non-expandable constructions, but no exact unrestricted formula for \(S(q,5)\) or \(N(q,5)\). A 2019 ternary-code paper whose abstract uses “maximum” was checked against its body: it proves non-expandability for arbitrary length and optimality only for length three; its length-five construction has 10 words rather than the known optimum 17. The 2026 \((t_1,t_2)\)-overlap-free paper was also checked in full and treats construction sizes and non-expandability, not the unrestricted maximum at length five. This result is therefore claimed **to the best of our knowledge** rather than as an exhaustive bibliographic guarantee.

The result is specific to block length five. It does not settle Blackburn's conjecture for arbitrary fixed length, nor does the proof directly extend to length six, where SQN has additional interacting levels.

## References

1. S. R. Blackburn, “Non-Overlapping Codes,” *IEEE Transactions on Information Theory* 61(9), 4890–4894 (2015). https://doi.org/10.1109/TIT.2015.2456634 ; preprint: https://arxiv.org/abs/1303.1026
2. L. Stanovnik, M. Moškon, M. Mraz, “In search of maximum non-overlapping codes,” *Designs, Codes and Cryptography* 92, 1299–1326 (2024). https://doi.org/10.1007/s10623-023-01344-z
3. L. Stanovnik, M. Moškon, M. Mraz, “On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths,” *Computational and Applied Mathematics* 44 (2025). https://doi.org/10.1007/s40314-024-03055-0
4. L. Stanovnik, “Codes with restricted overlaps: expandability, constructions, and bounds,” *Journal of Applied Mathematics and Computing* (2025). https://doi.org/10.1007/s12190-025-02441-z
5. H. Yang, Y. Ding, “Q-Ary \((t_1,t_2)\)-Overlap-Free Codes,” *IEICE Transactions on Fundamentals* E109-A(3), 757–762 (2026). https://doi.org/10.1587/transfun.2025EAL2050
6. M. Affaf, “Maximality on Construction of Ternary Cross Bifix Free Code,” *ComTech: Computer, Mathematics and Engineering Applications* 10(1), 23–27 (2019). https://doi.org/10.21512/comtech.v10i1.4716
