# A strict even-permutation bias in classical parking outcomes

## Finding

Let \(n\ge1\) cars, labeled \(1,\ldots,n\), enter a one-way street with \(n\) consecutively numbered parking spaces, in label order. Each car first tries its chosen space and, if necessary, advances to the first vacant space to the right. A preference list \(\alpha\in\{1,\ldots,n\}^n\) is a *parking function* when every car parks. Write \(\pi(\alpha)\in\mathfrak S_n\) for the *outcome permutation*: its entry at position \(j\) is the label of the car occupying space \(j\).

Define the signed enumerator, including the empty object, by
\[
S_0=1,\qquad S_n=\sum_{\alpha\in\mathrm{PF}_n}\operatorname{sgn}(\pi(\alpha))\quad(n\ge1).
\]
In the following formula, \(G(N,k)=\left[\begin{smallmatrix}N\\k\end{smallmatrix}\right]_{-1}\) denotes a Gaussian binomial coefficient evaluated as a polynomial at \(-1\); explicitly,
\[
G(N,k)=\begin{cases}
0,&N\text{ even and }k\text{ odd},\\
\displaystyle\binom{\lfloor N/2\rfloor}{\lfloor k/2\rfloor},&\text{otherwise},
\end{cases}\quad 0\le k\le N.
\]
**Theorem.** For every integer \(n\ge1\),
\[
\boxed{S_n=\sum_{j=1}^{n}j(-1)^{n-j}G(n-1,j-1)S_{j-1}S_{n-j},\qquad S_n>0.}
\]
Thus, under the uniform law on the \((n+1)^{n-1}\) classical parking functions,
\[
\boxed{\mathbb P(\pi\text{ even})-\mathbb P(\pi\text{ odd})
=\frac{S_n}{(n+1)^{n-1}}>0.}
\]
This is a strict, all-size bias of the *outcome* permutation, not the inversion parity of the preference word. The recurrence gives exact signed counts without enumerating all parking functions or all permutations.

A second, positivity-preserving description is obtained by separating even and odd lengths. Put
\[
E(z)=\sum_{m\ge0}S_{2m}\frac{z^m}{m!},\qquad
O(z)=\sum_{m\ge0}S_{2m+1}\frac{z^m}{m!}.
\]
These are **formal power series**; no positive radius of convergence is assumed. They satisfy
\[
\boxed{O=E^2+2zEE',\qquad E'=E^3+8zE^2E'+4z^2E^2E'',\qquad E(0)=1.}
\]
The positive coefficients on the right of the second identity yield an induction proving \(S_n>0\) for every \(n\), despite the alternating signs in the original recurrence.

## Assumptions and scope

The parking model is classical and deterministic conditional on preferences: exactly \(n\) unit-length cars and \(n\) spaces, arrivals in the order \(1,\ldots,n\), only forward search, and only preference lists for which everyone parks. No restriction is placed on preference multiplicities. The probability measure is uniform over valid preference lists, *not* uniform over resulting permutations. The parity is the sign of the order of occupants by increasing space number. The theorem covers all integers \(n\ge1\); \(n=0\) supplies only the combinatorial initial value.

## Proof

### 1. Decomposition at the last car

Fix \(n\ge1\), and suppose car \(n\) ultimately occupies space \(j\), where \(1\le j\le n\). Immediately before its arrival, every space except \(j\) is occupied. Its preference can therefore be any one of the \(j\) spaces \(1,\ldots,j\), providing a factor \(j\).

Let \(L\subseteq\{1,\ldots,n-1\}\) be the set of \(j-1\) earlier cars occupying spaces left of \(j\), and let \(R\) be its complement, of size \(n-j\). None of the cars occupying a right-hand space can have preferred a space \(\le j\): because space \(j\) remained vacant until the last arrival, that car would have stopped there. Likewise, any car occupying a left-hand space must have preferred a left-hand space. Hence the restrictions of the preference list to \(L\) and \(R\), with the right-hand preferences translated by \(j\), are independent classical parking functions of sizes \(j-1\) and \(n-j\). Conversely, any such pair of restricted parking functions, any subset \(L\) of the specified size, and any last preference \(\le j\), reconstructs a unique full parking function with the last car at \(j\).

Write \(\pi_L\) and \(\pi_R\) for the standardized outcome permutations within the two blocks. Define
\[
I(L)=\#\{(\ell,r)\in L\times R:\ell>r\}.
\]
When the two blocks are concatenated with the largest label \(n\) in between, there are \(I(L)\) cross-block inversions and \(n-j\) inversions contributed by car \(n\). Therefore
\[
\operatorname{sgn}(\pi)=(-1)^{I(L)+n-j}
\operatorname{sgn}(\pi_L)\operatorname{sgn}(\pi_R).
\]
Summing all preferences with fixed \(j,L\) gives
\[
j(-1)^{I(L)+n-j}S_{j-1}S_{n-j}.
\]

### 2. The signed subset sum

For \(0\le k\le N\), the polynomial
\[
\sum_{\substack{L\subseteq\{1,\ldots,N\}\\|L|=k}}q^{I(L)}
\]
is the Gaussian binomial coefficient \(\left[\begin{smallmatrix}N\\k\end{smallmatrix}\right]_q\). One can verify this directly using the recurrence obtained by considering the membership of the largest element, together with the boundary values \(G(0,0)=1\). At \(q=-1\), the standard Gaussian-binomial recurrence yields
\[
\left[\begin{smallmatrix}N\\k\end{smallmatrix}\right]_{-1}
=0\quad (N\text{ even},k\text{ odd}),
\]
and the ordinary-binomial expression stated above in all remaining cases. Consequently
\[
\sum_{|L|=j-1}(-1)^{I(L)}=G(n-1,j-1).
\]
Summing the fixed-position contribution over \(j=1,\ldots,n\) proves the exact recurrence for \(S_n\).

### 3. Parity separation and positive formal equations

Set \(E_m=S_{2m}\) and \(O_m=S_{2m+1}\) for \(m\ge0\). From the recurrence at odd sizes, \(G(2m,k)\) vanishes for odd \(k\), giving
\[
O_m=\sum_{a=0}^{m}(2a+1)\binom ma E_a E_{m-a}.
\]
At even sizes, for \(m\ge1\), the formula is
\[
E_m=\sum_{a=0}^{m-1}\binom{m-1}{a}
\Bigl((2a+2)O_aE_{m-1-a}-(2a+1)E_aO_{m-1-a}\Bigr).
\]
These are exact identities of integers. Passing to the exponential generating series in the new index \(m\), and using the ordinary product rule for formal derivatives, gives
\[
O=E^2+2zEE',\qquad E'=EO+2z(EO'-E'O).
\]
Substitution of the first identity into the second and simplification give
\[
E'=E^3+8zE^2E'+4z^2E^2E''.
\]
The initial coefficient is \(E_0=S_0=1\). Assume \(E_0,\ldots,E_m\) are positive. The coefficient of \(z^m\) on the left equals \(E_{m+1}/m!\). Each coefficient of \(z^m\) on the right is nonnegative and depends only on \(E_0,\ldots,E_m\): the prefactors \(z\) and \(z^2\) remove any dependence on \(E_{m+1}\) in the derivatives. Moreover the contribution from \(E^3\) is strictly positive, since it includes the term \(3E_m/m!\) for \(m\ge1\) (and equals \(1\) when \(m=0\)). Hence \(E_{m+1}>0\). This proves positivity of all even-indexed \(S_n\). The explicit positive convolution for \(O_m\) then proves positivity of all odd-indexed \(S_n\). The signed-count interpretation gives the claimed strict probability bias.

## Verification

Running `python3 verify.py` uses only the Python standard library and integer arithmetic. It checks the recurrence against direct simulation of every preference tuple for \(1\le n\le7\), including the classical cardinality \((n+1)^{n-1}\). It independently checks all permutations for \(1\le n\le8\) via the parking-outcome weight formula of Pinsky, tests the Gaussian-binomial specialization through ambient set size \(12\), and checks both parity-separated recurrences and the formal differential identity through degree \(14\). The script reports **209 exact assertions passed**. No random experiments, floating-point approximations, or external packages are needed.

The first signed values are
\[
(S_0,S_1,\ldots,S_{12})=(1,1,1,4,11,72,335,2944,19449,211520,1815089,23390208,247145107).
\]
The all-size positivity is established by the preceding formal-series induction, not by the finite checks.

## Relationship to prior work

Pinsky, *The distribution on permutations induced by a random parking function* (arXiv:2404.11529, Theorem 1), identifies the probability of each individual outcome permutation as a product of consecutive-record lengths divided by the total number of parking functions. That theorem is fully acknowledged: it implies an explicit, but factorial-size, signed sum. It does **not** give the all-size sign, the Gaussian-binomial convolution, or the positivity-preserving formal differential equation established here.

Paguyo and Yin, *Limit distributions for cycles of random parking functions* (arXiv:2502.07110), study cyclic structures of the **preference map** on labels; this is not the parity of the **occupied-space outcome permutation**. Celano and collaborators, *Inversions in parking functions* (arXiv:2508.11587), study inversions of the **preference words** and related word statistics, not the sign of the output permutation. Their inversion generating functions therefore do not specialize to this theorem. The distinction is important: parking preferences can repeat, while the outcome always permutes the car labels.

## Limitations

The theorem concerns only the sign of the output permutation, not its full inversion distribution. It gives an exact finite-size recurrence and a strict positivity statement, but no asymptotic expansion for the normalized bias or its decay rate. The formal power series need not converge analytically. No analogous statement is established here for other parking disciplines, weighted preferences, or fewer cars than spaces. A literature search does not rule out an unindexed or differently named equivalent identity; independent validation has not been performed.

## References

1. R. G. Pinsky, *The distribution on permutations induced by a random parking function*, arXiv:2404.11529 (first publicly posted 17 April 2024); *Electronic Journal of Combinatorics* 33 (2026), #P1.50. https://arxiv.org/abs/2404.11529
2. J. E. Paguyo and M. Yin, *Limit distributions for cycles of random parking functions*, arXiv:2502.07110 (first publicly posted 10 February 2025), math.PR, MSC 60C05 and 60F05. https://arxiv.org/abs/2502.07110
3. K. Celano, J. Elder, K. P. Hadaway, P. E. Harris, A. Priestley, and G. Udell, *Inversions in parking functions*, arXiv:2508.11587 (first publicly posted 15 August 2025). https://arxiv.org/abs/2508.11587
