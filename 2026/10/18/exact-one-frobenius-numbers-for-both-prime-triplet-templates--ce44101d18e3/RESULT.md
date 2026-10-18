# Exact one-Frobenius numbers for both prime-triplet templates

## Finding
For a triple \(A=(a,b,c)\) of positive integers, write \(d_A(N)\) for the number of ordered triples \((x,y,z)\in\mathbb Z_{\ge0}^3\) satisfying \(ax+by+cz=N\), and put
\[
g_1(A)=\max\{N\in\mathbb Z_{\ge0}:d_A(N)\le1\}.
\]
For each integer \(k\ge0\), define the two prime-triplet templates
\[
A_k=(6k+5,6k+7,6k+11),\qquad B_k=(6k+7,6k+11,6k+13).
\]
Then the exact one-Frobenius numbers are
\[
\boxed{g_1(A_k)=\begin{cases}24,&k=0,\\12k^2+40k+23,&k\ge1,\end{cases}}
\qquad
\boxed{g_1(B_k)=\begin{cases}45,&k=0,\\12k^2+50k+56,&k\ge1.\end{cases}}
\]
Neither primality nor the existence of infinitely many prime triplets is assumed. Consequently the formulas apply whenever the three entries in a template happen all to be prime.

## Assumptions and scope
The parameters are integers \(k\ge0\); representations use nonnegative coefficients and distinguish different coefficient triples. The generators in each template have greatest common divisor one, and their smallest generator is odd. The result concerns the threshold of at least **two** representations (the \(p=1\) generalized Frobenius number), not the ordinary Frobenius number \(p=0\) or general \(p\ge2\).

## Proof

**A second-baseline lemma.** Let \(a\) be the least generator of a coprime positive triple \((a,b,c)\). For each residue \(r\pmod a\), list with multiplicities, in increasing order, the integer costs \(by+cz\) for all \(y,z\ge0\) whose cost is congruent to \(r\pmod a\). Denote its second element by \(s_2(r)\). For any \(N\equiv r\pmod a\), the solutions of \(ax+by+cz=N\) correspond bijectively to those costs in this list not exceeding \(N\): the only possible \(x\) is \((N-by-cz)/a\). Thus the first integer of residue \(r\) with at least two representations is \(s_2(r)\). Since positive generators are coprime, the second cost exists in each residue; all larger integers in the same residue have at least two representations. Therefore
\[
g_1(a,b,c)=\max_{r\pmod a}s_2(r)-a.\tag{1}
\]

**First template.** Write \(a=6k+5\), \(b=a+2\), \(c=a+6\). Because
\[
by+cz=a(y+z)+2q,\qquad q=y+3z,
\]
and \(a\) is odd, the residue of the cost is in bijection with \(q\pmod a\). For fixed \(q=3u+s\), where \(u\ge0\) and \(s\in\{0,1,2\}\), the cheapest coefficient pair is \((y,z)=(s,u)\) and has cost
\[
f(3u+s)=uc+sb.\tag{2}
\]
Every other pair with the same \(q\) has cost \(f(q)+2at\) for some integer \(1\le t\le u\), since replacing one \(c\)-coin by three \(b\)-coins increases cost by \(3b-c=2a\). Direct substitution into (2) gives
\[
f(q+a)-f(q)=\begin{cases}(2k+1)c+2b,&q\equiv0\pmod3,\\(2k+2)c-b,&q\equiv1,2\pmod3.\end{cases}\tag{3}
\]
Both differences strictly exceed \(2a\) for all \(k\ge0\); hence they are positive, and the cheapest contribution from any larger \(q+a, q+2a,\ldots\) cannot precede an available second solution at the original \(q\).

Represent residues by \(q_0\in\{0,\ldots,a-1\}\). For \(q_0\ge3\), there is a second coefficient pair with the same \(q_0\), so \(s_2=f(q_0)+2a\). The largest \(f(q_0)\) in this range is
\[
f(a-1)=(2k+1)c+b.\tag{4}
\]
Indeed, the costs in each block \(3u,3u+1,3u+2\) are increasing, while successive blocks increase by \(c\); comparison of the last incomplete block with its predecessor gives (4), using \(c-b=4>0\). Thus this range contributes a maximum of \((2k+1)c+b+a=12k^2+40k+23\) to (1).

For the three residues \(q_0=0,1,2\), only one pair realizes \(q_0\), so \(s_2=f(q_0+a)\). Among these, the largest is at \(q_0=2\) and equals \((2k+2)c+b\), giving \((2k+2)c+b-a=12k^2+34k+24\) in (1). The first range wins by \(6k-1\) if \(k\ge1\); the second wins if \(k=0\). This proves the first boxed formula.

**Second template.** Now take \(a=6k+7\), \(b=a+4\), \(c=a+6\). Here
\[
by+cz=a(y+z)+2q,\qquad q=2y+3z.
\]
Again residues correspond bijectively to \(q\pmod a\). Every nonnegative \(q\ne1\) has a feasible pair; for fixed \(q\), choose the greatest nonnegative \(z\le q/3\) of parity \(q\), then \(y=(q-3z)/2\). This minimizes cost, because replacing two \(c\)-coins by three \(b\)-coins increases cost by \(3b-2c=a\). Write \(f(q)\) for this least cost. The complete table, with \(u\ge0\) and the \(6u+1\) line restricted to \(u\ge1\), is

| \(q\) | \(f(q)\) | maximizing \(z\) |
| --- | --- | --- |
| \(6u\) | \(2uc\) | \(2u\) |
| \(6u+1\) | \((2u-1)c+2b\) | \(2u-1\) |
| \(6u+2\) | \(2uc+b\) | \(2u\) |
| \(6u+3\) | \((2u+1)c\) | \(2u+1\) |
| \(6u+4\) | \(2uc+2b\) | \(2u\) |
| \(6u+5\) | \((2u+1)c+b\) | \(2u+1\) |

Comparing the table at \(q\) and \(q+a\) yields
\[
f(q+a)-f(q)=\begin{cases}(2k+1)c+2b,&q\equiv0,3\pmod6,\\(2k+3)c-b,&q\equiv1,2,4,5\pmod6,\end{cases}\tag{5}
\]
whenever \(f(q)\) is defined. Each increment is strictly greater than \(a\), and every later \(q+ja\) is still more expensive. Whenever the minimizing pair at the representative \(q_0\) has \(z\ge2\), the second cost in the residue is therefore exactly \(f(q_0)+a\).

The representatives \(q_0\in[0,a-1]\) not covered by this last case are \(q_0=0,1,2,3,4,5\), and \(q_0=7\) if \(k\ge1\). (At \(q_0=1\) there is no feasible pair at all.) For \(q_0=1\), the first pair occurs at \(q=a+1\) and already has \(z\ge2\), so \(s_2=f(a+1)+a\). At the remaining exceptional representatives, \(s_2=f(q_0+a)\). The corresponding contributions \(s_2-a\) to (1) are

| \(q_0\) | \(s_2-a\) |
| --- | --- |
| \(0\) | \((2k+1)c+2b-a\) |
| \(1\) | \((2k+2)c+b\) |
| \(2\) | \((2k+3)c-a\) |
| \(3\) | \((2k+2)c+2b-a\) |
| \(4\) | \((2k+3)c+b-a\) |
| \(5\) | \((2k+4)c-a\) |
| \(7\), only if \(k\ge1\) | \((2k+4)c+b-a\) |

For every nonexceptional representative, the contribution \(s_2-a=f(q_0)\) is at most \((2k+2)c\); the maximum follows directly from the six residue rows and is reached at \(q_0=a-1\). If \(k\ge1\), the exceptional \(q_0=7\) contribution strictly exceeds all six other exceptional contributions and the nonexceptional maximum: the differences are positive because \(a,b,c>0\) and \(2c-b=a+8>0\). Thus
\[
g_1(B_k)=(2k+4)c+b-a=12k^2+50k+56\quad(k\ge1).\tag{6}
\]
For \(k=0\), the representative \(7\) is not present; the remaining maximum occurs at \(q_0=5\) and is \(4c-a=45\). This proves the second formula. \(\square\)

## Verification
The standalone program `verify_prime_triplet_g1.py` is executable with Python 3 and has no third-party dependencies. It independently computes (i) the two smallest \(b y+c z\) baseline costs in each residue modulo \(a\), and (ii) all capped denumerants via an unbounded coin-change recurrence. The two independent routes verify both formulas for every \(0\le k<36\), or 72 complete parameter instances, including the two exceptional small cases. The finite verification is not used to justify the unbounded quantifier in the proof.

## Relationship to prior work
Robles-Pérez and Rosales [1], §§2–3, introduced the exact two prime-triplet template families as numerical semigroups and computed their ordinary Frobenius numbers, genus, Apéry sets, and pseudo-Frobenius numbers. Their Remark 2.4 explicitly proposes computation of \(p\)-Frobenius numbers for prime \(k\)-tuplets as future work. The present formulas solve the first positive threshold \(p=1\) in both of their prime-triplet template families; their \(p=0\) formulas are not claimed as new.

Komatsu and Ying [2], Theorem 1, derive \(p\)-Frobenius formulas for actual three-term arithmetic progressions \((a,a+d,a+2d)\). Neither template here is an arithmetic progression, as its two consecutive gaps are \((2,4)\) or \((4,2)\), so their theorem does not imply the boxed expressions. Liu and Xin [3] give an optimization method and explicit classical (zero-threshold) Frobenius formulas; their statements do not cover this positive representation threshold. The method of second residue baselines is related to general \(p\)-Apéry constructions, but the closed formulas and small-parameter transitions are additional arithmetic results.

## Limitations
The proof does not address \(p\ge2\) or prime quadruplets. It classifies the numerical templates without imposing primality; no assertion about the infinitude of prime triplets follows. Originality conclusions are restricted to the sources actually inspected, indexed mathematical searches, and accessible related findings; independently published equivalent formulas outside those sources remain possible. Independent mathematical validation has not been performed.

## References
[1] A. M. Robles-Pérez and J. C. Rosales, *A Frobenius problem suggested by prime k-tuplets (extended version)*, arXiv:2112.05501 (first posted 2021-12-10), especially Remark 2.4 and §§3.1–3.2. https://arxiv.org/abs/2112.05501

[2] T. Komatsu and H. Ying, *The p-numerical semigroup of the triple of arithmetic progressions*, arXiv:2206.13052 (first posted 2022-06-27), particularly Theorem 1 and Lemma 1. https://arxiv.org/abs/2206.13052

[3] F. Liu and G. Xin, *A combinatorial approach to Frobenius numbers of some special sequences (complete version)*, arXiv:2303.07149 (first posted 2023-03-13), especially §2. https://arxiv.org/abs/2303.07149
