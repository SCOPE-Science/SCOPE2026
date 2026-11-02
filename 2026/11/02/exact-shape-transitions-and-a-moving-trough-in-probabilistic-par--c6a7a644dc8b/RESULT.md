# Exact shape transitions and a moving trough in probabilistic parking preferences

## Finding

For each integer \(n\ge2\), independently choose the preferences \(a_1,\ldots,a_n\) uniformly from \(\{1,\ldots,n\}\). Cars arrive in that order. A car parks at its preference if empty; otherwise it tosses a Bernoulli coin, searches forward for the nearest unoccupied space with probability \(p\), or backward with probability \(1-p\), and fails if its chosen direction offers no vacancy. Let \(S\) mean that all cars park, and define
\[
Q_{n,p}(j)=\Pr(a_n=j\mid S),\qquad 1\le j\le n,\quad 0\le p\le1.
\]

Define the increasing sequence \(h_k=(1+1/k)^{k-1}\) for \(k\ge1\), and thresholds
\[
t_{n,j}=\frac{h_j}{h_j+h_{n-j}},\qquad 1\le j<n.
\]
Then the following **complete shape classification** holds:

1. The thresholds satisfy \(t_{n,1}<\cdots<t_{n,n-1}\) for \(n\ge3\), with \(t_{n,j}+t_{n,n-j}=1\). The adjacent probability difference has the sign of \(t_{n,j}-p\), with equality if and only if \(p=t_{n,j}\). Thus \(Q_{n,p}\) is either strictly monotone, or decreases and then increases, with at most two tied adjacent minima. In particular, it has no strict interior maximum.
2. The distribution is strictly increasing if \(p<t_{n,1}\) and strictly decreasing if \(p>t_{n,n-1}\). At either boundary it has one tied adjacent pair. In the interior range its trough is uniquely determined by which adjacent thresholds bracket \(p\). Its maximum always occurs at an endpoint: uniquely at \(n\) for \(p<1/2\), uniquely at \(1\) for \(p>1/2\), and at both endpoints for \(p=1/2\) (for \(n=2\), both entries are tied at \(p=1/2\)).
3. The extreme boundaries converge to
\[
\lim_{n\to\infty}t_{n,1}=\frac1{1+e},\qquad
\lim_{n\to\infty}t_{n,n-1}=\frac{e}{1+e}.
\]
For fixed \(0\le p<1/2\), define \(\tau_0=0\) and \(\tau_k=h_k/(h_k+e)\) for \(k\ge1\). If \(\tau_{k-1}<p\le\tau_k\), then for all sufficiently large \(n\), the unique minimum is at position \(k\). At \(p=0\) it is at position \(1\). For fixed \(p>1/2\), reflect this description using \(1-p\): the minimum is at \(n+1-k\). At \(p=1/2\) the minimum is central (two equal central entries for even \(n\)).
4. A distinct, **macroscopic trough-migration window** occurs when \(p_n=1/2+t/n\), for any fixed real \(t\). If \(m_n\) is any minimizing position of \(Q_{n,p_n}\), then
\[
\boxed{\frac{m_n}{n}\longrightarrow u(t):=\frac12+\frac{t}{\sqrt{9/4+4t^2}+3/2}.}
\]
The function \(u\) increases continuously from \(0\) to \(1\), with \(u(0)=1/2\). The finite-size boundary thresholds have a nontrivial limiting accumulation at \(1/2\), while the macroscopic minimum moves across the whole street on the \(1/n\) probability scale.

## Assumptions and scope

The parking rule uses one independent direction coin only when the desired space is already occupied. Searching then stops at the first vacancy in that direction; a car does not reverse after an unsuccessful search. Preferences are independent and uniform before conditioning on \(S\). Probability \(\Pr(S)>0\) for every \(n\ge2\) and \(p\in[0,1]\), since permutation preferences always succeed. The theorem covers all \(n\ge2\) and all \(p\in[0,1]\), including parameter values giving adjacent ties. In asymptotic statements \(n\to\infty\); \(t\) is fixed in the moving-window assertion.

## Proof

**1. Exact vacant-space weights.** Suppose the first \(n-1\) cars have all parked, leaving only space \(k\) empty. Their preferences split into a shuffled \((k-1)\)-car parking process to the left and an \((n-k)\)-car process to the right: no car can cross the vacant space. The expected counts of successful preference lists on these two substreets are respectively \(k^{k-2}\) and \((n-k+1)^{n-k-1}\). These standard circular-rotation counts remain valid for every direction parameter (the weighted success count does not depend on it). Therefore the expected number of first-stage preference lists leaving exactly \(k\) empty is
\[
c_{n,k}=\binom{n-1}{k-1}\,k^{k-2}(n-k+1)^{n-k-1}.
\]
An exponent \(-1\) with base \(1\) is interpreted as \(1\), corresponding to an empty substreet. Independently conditioning on the last preference \(j\), the final car succeeds with weight \(1\) when \(j=k\), with weight \(p\) when \(j<k\), and with weight \(1-p\) when \(j>k\). The known parking-success count is \((n+1)^{n-1}\), independently of \(p\), yielding the exact conditional law
\[
Q_{n,p}(j)=\frac{c_{n,j}+p\sum_{k=j+1}^{n}c_{n,k}+(1-p)\sum_{k=1}^{j-1}c_{n,k}}{(n+1)^{n-1}}. \tag{1}
\]
This is the previously established last-preference distribution of Durmić, Han, Harris, Ribeiro and Yin (2022, Theorem 3), reproduced to make the subsequent argument auditable. Its normalization follows either from their binomial identity or the circular rotation proof for the complete parking event.

**2. One-step factorization and strict log-convexity.** Taking adjacent differences in (1) gives
\[
Q_{n,p}(j+1)-Q_{n,p}(j)
=\frac{(1-p)c_{n,j+1}-pc_{n,j}}{(n+1)^{n-1}}. \tag{2}
\]
Writing \(w_s=c_{n,n-s}=\binom{n-1}{s}(n-s)^{n-s-2}(s+1)^{s-1}\), direct factorial cancellation shows
\[
\frac{w_s}{w_{s-1}}=\frac{h_s}{h_{n-s}},\quad 1\le s<n,\qquad
h_k=\left(1+\frac1k\right)^{k-1}. \tag{3}
\]
In particular,
\[
\frac{c_{n,j+1}}{c_{n,j}}
=\frac{h_j}{h_{n-j}},\qquad
Q_{n,p}(j+1)>Q_{n,p}(j)\iff p<\frac{h_j}{h_j+h_{n-j}}. \tag{4}
\]
To show strict increase of \(h_k\), let \(f(x)=(x-1)\log(1+1/x)\) for real \(x\ge1\). Then
\[
f'(x)=\log(1+1/x)-\frac{x-1}{x(x+1)}>\frac1{x+1}-\frac{x-1}{x(x+1)}>0.
\]
The first inequality follows from \(\log(1+y)>y/(1+y)\) for \(y>0\). Hence \(h_k\) strictly increases, while \(h_{n-j}\) strictly decreases with \(j\), proving \(t_{n,j}\) strictly increases. Equation (4) now proves all one-trough shape and tie statements. Reflection \(t_{n,j}+t_{n,n-j}=1\) is immediate.

**3. Endpoint maxima.** By (1), symmetry \(c_{n,k}=c_{n,n+1-k}\) gives
\[
Q_{n,p}(n)-Q_{n,p}(1)
=\frac{(1-2p)\sum_{k=2}^{n}c_{n,k}}{(n+1)^{n-1}}. \tag{5}
\]
The sum is strictly positive. Since the distribution has no interior maximum, (5) determines the global maximizing endpoint for \(p\ne1/2\), and both endpoints maximize when \(p=1/2\). The assertion for \(n=2\) follows directly from (2).

**4. Fixed-bias boundary layers.** Since \(h_k\to e\), the extreme thresholds tend to \(1/(1+e)\) and \(e/(1+e)\), and for each fixed \(j\),
\[
t_{n,j}\longrightarrow \tau_j:=\frac{h_j}{h_j+e}<\frac12.
\]
The numbers \(\tau_j\) increase strictly to \(1/2\). Moreover \(t_{n,j}>\tau_j\) for all sufficiently large \(n>j\), because \(h_{n-j}<e\). If \(\tau_{k-1}<p\le\tau_k\), then \(t_{n,k-1}<p\le t_{n,k}\) eventually (the lower bound is omitted for \(k=1\)); equation (4) places the unique trough at \(k\). Reflection gives the right boundary, and exact threshold symmetry gives the central trough at \(p=1/2\).

**5. Moving-window limit.** Taylor expansion yields
\[
\log h_k=1-\frac{3}{2k}+O(k^{-2}),\qquad k\to\infty.
\]
Uniformly when \(j/n\) belongs to any compact subinterval of \((0,1)\), it follows that
\[
t_{n,j}=\frac12+\frac38\left(\frac1{n-j}-\frac1j\right)+O(n^{-2}). \tag{6}
\]
Thus for \(j/n\to x\in(0,1)\),
\[
n(t_{n,j}-1/2)\longrightarrow F(x):=\frac38\left(\frac1{1-x}-\frac1x\right).
\]
Here \(F\) is continuous and strictly increasing from \(-\infty\) to \(+\infty\). For fixed \(t\), the sign rule (4) and the monotonic threshold sequence trap every minimizing index between positions with limiting fractions just below and just above the unique solution of \(F(x)=t\). Elementary inversion gives \(x=u(t)\) as displayed. This proves the scaling assertion even when a finite distribution has two tied minimizing entries.

## Verification

The accompanying standalone Python checker independently enumerates all preference vectors and all direction-choice paths (with exact rational weights) for \(2\le n\le6\) and seven rational values of \(p\). It compares the resulting conditional law to (1), verifies the adjacent differences and sign thresholds, checks the binomial weight ratio and strict threshold order through \(n=80\), and checks the moving-window profile numerically for larger \(n\). The checker passes 6,849 assertions, including direct enumeration of 350,476 preference vectors counted across parameter choices. These finite calculations are corroboration, not a substitute for the unrestricted analytical proof. Run `python3 verify_parking_shapes.py` from the extracted package directory.

## Relationship to prior work

Durmić, Han, Harris, Ribeiro and Yin obtained the complete finite conditional last-preference law (1), the parameter-independent success probability, expected-preference asymptotics and total-variation rates. Those are explicitly **prior** results, not claimed here. Tian and Treviño independently studied the same random-direction protocol but their original model result concerns the total expected success count. Harris, Ribeiro and Yin later extended the exact preference law to unequal numbers of cars and spaces; this contains the model with equal numbers. The present assertion is the discrete-log-convexity classification of the shape of those probability masses, all exact shape-change thresholds, the accumulating endpoint layers, and the new \(p-1/2=O(1/n)\) macroscopic trough law. These require analysis distinct from printing the previously known probability formula. Existing exact distribution results make implicit derivability a substantial priority risk; they do not, in the examined original texts, state this shape-and-scaling classification.

## Limitations

This result addresses only the one-coin bidirectional protocol with uniform independent preferences and equal numbers of cars and spaces. It does not address the joint law of different cars' preferences, nonuniform preference distributions, several direction tosses per unsuccessful search, or extra vacant spots. The finite conditional probability distribution and the parking-shuffle enumeration are established prior work; mathematical originality is claimed only for the shape classifications and moving-trough scaling. Any unstated derivation in earlier general formula literature remains a historical-priority risk. The scientific assessment is a self-review, not independent validation.

## References

1. I. Durmić, A. Han, P. E. Harris, R. Ribeiro and M. Yin, *Probabilistic Parking Functions*, arXiv:2211.00536v1 (first public November 1, 2022), Theorem 3 and Section 2.4; *Electronic Journal of Combinatorics* 30(3), P3.18 (2023). https://arxiv.org/html/2211.00536v1
2. M. Tian and E. Treviño, *Generalizing parking functions with randomness*, arXiv:2111.12850 (2021), Section 2. https://arxiv.org/abs/2111.12850
3. P. E. Harris, R. Ribeiro and M. Yin, *Probabilistic (m,n)-Parking Functions*, arXiv:2502.00269 (2025), Theorem 2.7 and Section 3. https://arxiv.org/abs/2502.00269
