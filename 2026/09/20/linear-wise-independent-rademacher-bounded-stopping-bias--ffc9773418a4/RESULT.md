# Square-root bounded-stopping bias under linear-wise independent Rademacher increments

## Result

Let \(X_1,\ldots,X_{m+\ell}\in\{-1,+1\}\) be fair Rademacher variables. Assume that the first block \((X_1,\ldots,X_m)\) is mutually independent and that the second block \((X_{m+1},\ldots,X_{m+\ell})\) is mutually independent. Cross-block dependence is otherwise unrestricted. Put
\[
S_t=\sum_{i=1}^tX_i,
\qquad
M_\ell=\max_{0\le j\le\ell}\sum_{i=1}^j\varepsilon_i,
\]
where \(\varepsilon_1,\ldots,\varepsilon_\ell\) are iid fair signs, and write \(a_\ell=\mathbb E M_\ell\).

For every stopping time \(T\) for the natural filtration with
\[
m\le T\le m+\ell,
\]
one has the sharp envelope
\[
\boxed{|\mathbb E S_T|\le a_\ell.}
\]
In fact the upper inequality holds for every random index taking values in \([m,m+\ell]\), whether or not it is a stopping time.

The constant has the closed form
\[
a_{2r}=\left(2r+\frac12\right)\frac{\binom{2r}{r}}{4^r}-\frac12,
\qquad
a_{2r+1}=(2r+1)\frac{\binom{2r}{r}}{4^r}-\frac12,
\]
and therefore
\[
a_\ell=\sqrt{\frac{2\ell}{\pi}}-\frac12+O(\ell^{-1/2}).
\]

The sharpness can coexist with very high limited independence. Let \(A\) be an \(m\times\ell\) full-column-rank matrix over \(\mathbb F_2\), let \(U\) be uniform on \(\mathbb F_2^m\), and define
\[
X_i=(-1)^{U_i},\quad 1\le i\le m,
\qquad
X_{m+j}=(-1)^{\langle A_{\cdot j},U\rangle},\quad 1\le j\le\ell.
\]
The first block reveals \(U\), hence it reveals the entire second block. The second block is nevertheless iid because the columns of \(A\) are linearly independent.

Define
\[
d(A)=\min_{0\ne y\in\mathbb F_2^\ell}\bigl(\operatorname{wt}(y)+\operatorname{wt}(Ay)\bigr).
\]
Then the full family \(X_1,\ldots,X_{m+\ell}\) is \((d(A)-1)\)-wise independent. For every \(k<d(A)\), the stopping rule that, at time \(m\), chooses the first location of the maximum of the already measurable second-block partial sums satisfies
\[
\mathbb E S_T=a_\ell.
\]
Choosing the first location of the minimum gives \(-a_\ell\).

A sufficient existence criterion is
\[
\frac{1}{2^m-1}
\sum_{a=1}^{\min(\ell,k-1)}\binom{\ell}{a}
\sum_{b=1}^{\min(m,k-a)}\binom{m}{b}<1.
\]
Indeed, for a uniformly chosen injective linear map \(A:\mathbb F_2^\ell\to\mathbb F_2^m\), each fixed nonzero \(y\) has \(Ay\) uniform over the nonzero vectors of \(\mathbb F_2^m\); the displayed quantity is the expected number of nonzero \(y\) producing a relation of weight at most \(k\). In particular, the simpler condition
\[
\sum_{j=2}^{k}\binom{m+\ell}{j}<2^m-1
\]
is sufficient.

## Linear-wise independence still permits square-root stopping bias

Let \(N=m+\ell\), let \(h_2(x)=-x\log_2x-(1-x)\log_2(1-x)\), and fix \(0<\delta<1/2\). For any
\[
0<R<\min\left\{\frac12,1-h_2(\delta)\right\},
\]
take \(\ell=\lfloor RN\rfloor\) and \(m=N-\ell\). The binomial entropy bound implies that, for all sufficiently large \(N\), an \(A\) exists with \(d(A)>\lfloor\delta N\rfloor\). Consequently there are \(\lfloor\delta N\rfloor\)-wise independent fair Rademacher increments and a bounded stopping time \(T\le N\) for which
\[
\mathbb E S_T
=\sqrt{\frac{2R}{\pi}}\sqrt N-\frac12+o(1).
\]
Thus a fixed positive fraction of full independence, even arbitrarily close to one half, does not restore the zero-bias conclusion of bounded optional stopping.

There is also an explicit boundary family. For \(N=2^r-1\), put a binary simplex code \([N,r,2^{r-1}]\) in systematic form and use it as the relation code \(\{(Ay,y):y\in\mathbb F_2^r\}\). Then the resulting \(N\) signs are
\[
\left(2^{r-1}-1\right)=\frac{N-1}{2}
\]
-wise independent, the final \(r\) signs are iid and measurable from the first \(N-r\), and a bounded stopping time achieves
\[
\mathbb E S_T=a_r\sim\sqrt{\frac{2\log_2N}{\pi}}.
\]
Hence the stopping bias can still diverge at essentially half-wise independence.

Finally, Narayanan's established four-wise maximal inequality gives
\[
\mathbb E\max_{t\le N}|S_t|^2=O(N)
\]
for four-wise independent Rademacher increments. Therefore, if
\[
B_{N,k}=\sup |\mathbb E S_T|,
\]
where the supremum ranges over all \(k\)-wise independent fair Rademacher increments and all stopping times \(T\le N\), then for every fixed \(0<\delta<1/2\),
\[
\boxed{B_{N,\lfloor\delta N\rfloor}=\Theta_\delta(\sqrt N).}
\]
The upper bound is inherited from the known four-wise maximal theorem; the lower bound is the construction above. No sharp global constant is claimed.

## Proof of the two-block envelope

Write \(T=m+K\), where \(0\le K\le\ell\). If
\[
R_j=\sum_{i=1}^jX_{m+i},
\]
then pathwise
\[
\min_{0\le j\le\ell}R_j\le R_K\le\max_{0\le j\le\ell}R_j.
\]
Since \(\mathbb ES_m=0\) and the second block has the ordinary iid simple-walk law,
\[
-a_\ell\le\mathbb E(S_m+R_K)\le a_\ell.
\]
This proves the universal bound.

For the linear construction, the first block is the coordinate character basis, so observing it determines \(U\) and hence all future signs. Let \(K\) be the first maximizer of \(R_j\). Then \(K\) is measurable at time \(m\), so \(T=m+K\) is a stopping time, and
\[
S_T=S_m+M_\ell.
\]
Taking expectations yields \(\mathbb ES_T=a_\ell\).

For the independence claim, a subfamily of the characters is mutually independent exactly when its coefficient vectors are linearly independent over \(\mathbb F_2\). A linear relation among columns of \([I_m\ A]\) has the form
\[
x+Ay=0,
\]
so its Hamming weight is \(\operatorname{wt}(Ay)+\operatorname{wt}(y)\). Thus the least dependent subfamily has size \(d(A)\).

For the closed form of \(a_\ell\), the reflection principle gives, for integer \(j\ge1\),
\[
\Pr(M_\ell\ge j)=\Pr(S_\ell\ge j)+\Pr(S_\ell\ge j+1).
\]
Summation over \(j\) yields
\[
a_\ell=\mathbb E|S_\ell|-\Pr(S_\ell>0),
\]
from which the displayed central-binomial formulas follow.

## Concrete elementary extremizers

For equal halves \(m=\ell\), pairwise-independent sharpness is available for every \(m\ge3\). For even \(m\), take the second coefficient basis
\[
f_i=\mathbf 1+e_i,\qquad 1\le i\le m,
\]
where \(\mathbf1\) is the all-ones vector. This basis has relation distance four, so the complete \(2m\)-sign family is actually three-wise independent and still attains \(a_m\). For odd \(m\), one may use
\[
f_i=e_i+e_m\ (i<m),\qquad f_m=e_1+\cdots+e_m,
\]
which is a basis disjoint from the coordinate basis and gives pairwise independence.

## Interpretation

The result does not contradict the optional stopping theorem. Under mutual independence the partial-sum process is a martingale for its natural filtration, whereas the constructed limited-independent process is not: collectively, the past can determine future increments even though every small subfamily is independent. The point is quantitative: low-order or even linear-order independence is not a substitute for the conditional-mean hypothesis needed by martingale stopping arguments.

## Relation to prior literature and originality scope

Wald's stopped-sum theory is classical. Joffe (1971) showed that pairwise-independent variables can be almost deterministic collectively, and Benjamini--Kozma--Romik (2006) constructed pairwise-independent sign walks with highly nonclassical path behavior using Walsh/Gray-code ideas. Narayanan (2022) determined sharp-order maximal-moment phenomena for limited-independent random walks, including a four-wise maximal second-moment bound. Binary linear codes and their connection to k-wise independent sample spaces are also standard.

The claim of novelty is therefore restricted. To the best of our knowledge, the literature checked does not state the exact two-iid-block stopping envelope above, its realization by a future block completely measurable at the block boundary, the systematic-code criterion that preserves the sharp endpoint under linear-wise independence, or the resulting \(\Theta(\sqrt N)\) worst-case bounded-stopping bias for every fixed independence fraction below one half. These are the proposed new contributions; the underlying Walsh-character, coding, reflection, and maximal-inequality ingredients are not claimed as new.

A residual originality risk remains that an equivalent result appears under the language of orthogonal arrays, resilient Boolean functions, pseudorandom stopping rules, or older optimal-stopping counterexamples. The search also found modern prophet-inequality work under pairwise-independent priors, but that problem selects individual revealed rewards rather than the value of a stopped partial sum and does not supply the envelope above.

## Limitations

The exact constant \(a_\ell\) is sharp for the two-block class with each block iid and stopping restricted to the second block. It is not claimed to be the sharp constant over all limited-independent walks of length \(N\). The global statement gives the correct \(\sqrt N\) order for fixed \(\delta<1/2\), not an optimal leading constant. The high-independence lower construction is binary and uses a coding-theoretic existence argument; the simplex boundary family is explicit only along \(N=2^r-1\).

## Reproducibility

`artifacts/verify_stopping_bias.py` uses exact integer and rational arithmetic to check the elementary equal-block constructions, their relation distances and stopped expectations for small dimensions; verifies the simplex-code relation distance for several values of \(r\); and tabulates the finite binomial sufficient condition. `artifacts/VERIFICATION.txt` records the verified outputs.

## References

1. A. Wald, *On Cumulative Sums of Random Variables*, Ann. Math. Statist. 15 (1944), 283--296. https://doi.org/10.1214/aoms/1177731235
2. A. Joffe, *On a Sequence of Almost Deterministic Pairwise Independent Random Variables*, Proc. Amer. Math. Soc. 29 (1971), 381--382. https://doi.org/10.2307/2038147
3. Y. H. Wang, *Dependent Random Variables with Independent Subsets -- II*, Canad. Math. Bull. 33 (1990), 24--28. https://doi.org/10.4153/CMB-1990-004-6
4. I. Benjamini, G. Kozma, D. Romik, *Random walks with k-wise independent increments*, Electron. Commun. Probab. 11 (2006), 100--107. https://doi.org/10.1214/ECP.v11-1201
5. S. Narayanan, *Three-wise independent random walks can be slightly unbounded*, Random Structures Algorithms 61 (2022), 573--598. https://doi.org/10.1002/rsa.21075
6. A. Gupta, J. Hu, G. Kehne, R. Levin, *Pairwise-independent contention resolution*, Mathematical Programming (2025). https://doi.org/10.1007/s10107-025-02253-w

**Same-model review: passed. Independent audit: not yet performed.**
