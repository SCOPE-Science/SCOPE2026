# Exact beta-binomial discord and rare logarithmic dissent on a zealot-pinned voter star

## Finding

**Theorem.** Let \(m\ge1\). Consider a star with one updating hub, \(m\) updating follower leaves and two non-updating leaves fixed at opposite binary opinions. Every updating vertex has an independent rate-one exponential clock and, upon ringing, copies a uniformly selected neighbor. Let \(H\in\{0,1\}\) be the hub opinion and \(K\) the number of follower leaves holding opinion one. Put \(\alpha=1/(m+3)\), and let \((a)_r=a(a+1)\cdots(a+r-1)\) for \(r\ge1\), with \((a)_0=1\). The unique stationary distribution is

\[
\Pr(H=0,K=k)=\frac12\binom{m}{k}\frac{(\alpha)_k(1+\alpha)_{m-k}}{(1+2\alpha)_m},\qquad
\Pr(H=1,K=k)=\frac12\binom{m}{k}\frac{(1+\alpha)_k(\alpha)_{m-k}}{(1+2\alpha)_m},
\quad 0\le k\le m.
\]

The number \(M\) of updating leaves disagreeing with the hub has the **exact beta-binomial law**
\[
\Pr(M=k)=\binom{m}{k}\frac{(\alpha)_k(1+\alpha)_{m-k}}{(1+2\alpha)_m}\quad(0\le k\le m).
\]
Its mean and variance are
\[
\mathbb E M=\frac{m}{m+5},\qquad
\operatorname{Var}(M)=\frac{m(m+1)}{2(m+5)}-\left(\frac{m}{m+5}\right)^2.
\]
In particular, the typical configuration has zero follower dissent despite \(\mathbb E M\to1\) and \(\operatorname{Var}(M)\sim m/2\). Writing \(H_m=\sum_{j=1}^m1/j\),
\[
\Pr(M>0)=\frac{H_m}{m+3}\left(1+O\!\left(\frac{H_m}{m}\right)\right),\qquad
\sup_{1\le k\le m}\left|\frac{\Pr(M=k\mid M>0)}{1/(kH_m)}-1\right|
=O\!\left(\frac{H_m}{m}\right).
\]
Consequently, given nonzero dissent, \(\log M/\log m\) converges in distribution to the uniform law on \([0,1]\), and \(\mathbb E[M\mid M>0]\sim m/\log m\) as \(m\to\infty\).

## Assumptions and scope

The contact graph is the specified star with exactly two fixed, oppositely opinionated leaves and \(m\) *updating* leaves. Only updating vertices ring, at rate one independently; neighbors are chosen uniformly from all graph neighbors. There is no spontaneous opinion change, no noise beyond copying, and no self-neighbor. The stationary statement is for finite \(m\ge1\). The asymptotic statements are for integer \(m\to\infty\). The zero-dissent event refers only to updating follower leaves, not to the two stubborn leaves. The two stubborn leaves always disagree with one another. Because the finite full configuration chain is irreducible, its stationary distribution is invariant under permutations of the \(m\) follower labels. The displayed joint law concerns the hub and follower count, and it determines the stationary microstate law by uniformly distributing the count mass over follower subsets of the indicated size.

## Proof

**1. State transitions and uniqueness.** In state \((0,k)\), the updating leaves holding one revert to zero at total rate \(k\), and the hub becomes one at rate \((k+1)/(m+2)\). In state \((1,k)\), the updating leaves holding zero become one at total rate \(m-k\), and the hub becomes zero at rate \((m-k+1)/(m+2)\). The latter hub rates count one stubborn leaf of the opposite opinion. These rates define the lumped continuous-time chain on \(\{0,1\}\times\{0,\ldots,m\}\). All hub flips have positive rates; while the hub is held at either opinion every follower can be made to match it through positive-rate paths, so the chain is irreducible. The full labeled chain is also irreducible, by flipping the hub through its stubborn neighbors and then updating any specified subset of followers. Uniqueness follows.

**2. Exact stationary law.** Write \(a_k=\Pr(H=0,K=k)\), \(b_k=\Pr(H=1,K=k)\) in stationarity. Global opinion complementation accompanied by exchange of the stubborn labels gives \(b_k=a_{m-k}\). Summing stationarity equations for \(K\le k\), for \(0\le k<m\), shows that flux across the cut is balanced:
\[
(k+1)a_{k+1}=(m-k)b_k.
\]
The \((0,k)\) stationary balance equation, for \(0\le k<m\), is
\[
\left(k+\frac{k+1}{m+2}\right)a_k=(k+1)a_{k+1}+\frac{m-k+1}{m+2}b_k.
\]
Eliminating \(b_k\) gives the recursion
\[
\frac{a_{k+1}}{a_k}=\frac{m-k}{k+1}\frac{k+\alpha}{m-k+\alpha},\qquad \alpha=\frac1{m+3}.
\]
The proposed beta-binomial weights obey this recursion. They also obey the cut identity directly: using \((1+\alpha)_r=(\alpha)_{r+1}/\alpha\), one gets \((k+1)a_{k+1}=(m-k)a_{m-k}\). The preceding stationary equations and the boundary equation at \((0,m)\) therefore hold; the equations for \(H=1\) follow by complementation. Normalization uses the finite rising-factorial Vandermonde identity
\[
\sum_{k=0}^m\binom mk(a)_k(b)_{m-k}=(a+b)_m,
\]
which follows by comparing coefficients of \(t^m\) in \((1-t)^{-a}(1-t)^{-b}=(1-t)^{-(a+b)}\). Each hub state has mass \(1/2\). Thus the displayed law satisfies all equations and is the unique stationary law.

**3. Discord law and moments.** When \(H=0\), the dissent count is \(K\); when \(H=1\), it is \(m-K\). Complementation makes the two conditional distributions identical. The beta-binomial expression follows. The rising-factorial mixture or factorial-moment identity yields
\[
\mathbb E[(M)_r^{\rm falling}]= (m)_r^{\rm falling}\frac{(\alpha)_r}{(1+2\alpha)_r},\qquad 0\le r\le m.
\]
In particular \(\mathbb E M=m\alpha/(1+2\alpha)=m/(m+5)\) and \(\mathbb E[M(M-1)]=m(m-1)/(2(m+5))\); the displayed variance follows from \(M^2=M(M-1)+M\). The growth \(\operatorname{Var}(M)\sim m/2\) is immediate.

**4. Rare, logarithmically spread discord.** For any \(m\), let \(H_m=\sum_{j=1}^{m}1/j\). Directly from the exact law,
\[
\Pr(M=0)=\prod_{j=1}^m\frac{1+\alpha/j}{1+2\alpha/j}.
\]
Using \(\log(1+x)=x+O(x^2)\) uniformly for \(0\le x\le1\), one gets \(\log\Pr(M=0)=-\alpha H_m+O(\alpha^2)\), as \(\sum_{j\ge1}j^{-2}<\infty\). Therefore \(\Pr(M>0)=\alpha H_m(1+O(\alpha H_m))\). For \(1\le k\le m\), cancellation of factorials gives the exact identity
\[
\Pr(M=k)=\frac{\alpha}{k}
\frac{\prod_{j=1}^{k-1}(1+\alpha/j)\prod_{j=1}^{m-k}(1+\alpha/j)}{\prod_{j=1}^{m}(1+2\alpha/j)}.
\]
The logarithm of the product ratio has absolute value at most \(4\alpha H_m\), since \(0\le\log(1+x)\le x\). The ratio is thus \(1+O(\alpha H_m)\), uniformly in \(k\). Dividing by the positive-dissent probability yields the asserted uniform relative approximation by harmonic weights \(1/(kH_m)\), hence total-variation error \(O(\log m/m)\). For each \(0\le t\le1\), \(H_{\lfloor m^t\rfloor}/H_m\to t\) (at \(t=0\), the numerator is \(1\) and the ratio tends to zero). This proves \(\log M/\log m\Rightarrow\operatorname{Uniform}[0,1]\) conditionally on \(M>0\). Finally \(\mathbb E[M\mid M>0]=\mathbb E M/\Pr(M>0)\sim m/\log m\).

## Verification

The accompanying `VERIFY.py` reconstructs the exact finite Markov generator from the transition rates using rational arithmetic, solves the stationary linear system independently by Gaussian elimination, and checks equality with the closed form, all stationary balance equations, the two factorial-moment identities, and normalization for each \(1\le m\le7\). Running `python VERIFY.py` emits the contents of `certificate.json` byte-for-byte. These finite checks are diagnostic only: the proof above establishes the claims for every finite \(m\) and the asymptotic regime.

## Relationship to prior work

Mobilia, Petersen and Redner [1] analyzed zealot-pinned voter dynamics on homogeneous spatial and well-mixed settings. Acemoglu, Ozdaglar and coauthors [2,3] developed general linear and coalescing-walk methods for stubborn-agent networks and their moments. Mori, Hisakado and Nakayama [4] obtained multivariate-beta limits for a model with large local populations and, in Appendix B, the classical beta-binomial distribution on complete graphs. Those results provide the models and general tools, but the examined statements do not yield the present **finite star with pendant stubborn leaves** joint law or its rare, logarithmically spread follower-dissent asymptotics. A later paper [5] studies the influence of stubborn agents on diverse networks via opinion expectations rather than this complete stationary law. The mathematical distribution family is familiar; what is asserted as a new contribution is the exact star-specific parameter \(1/(m+3)\), the conditional hub/count law, and the associated rare-disagreement scaling, not the existence of beta-binomial distributions generally.

## Limitations

These are mathematical predictions for a precisely specified neutral-copying social model, not evidence about human voters. A different update convention (for example, uniform undirected edge rings rather than one vertex clock per updating vertex), moving stubborn agents, weighted interactions, or additional links among followers changes the generator. The law is not claimed for those variants. Earlier derivations of the same law under another terminology cannot be ruled out without independent bibliographic examination; the result is not independently certified. The asymptotic law is conditional on the atypical event of positive follower discord.

## References

[1] Mobilia, Petersen and Redner, *On the Role of Zealotry in the Voter Model* (2007), arXiv:0706.2892v1, https://arxiv.org/abs/0706.2892.

[2] Yildiz, Acemoglu, Ozdaglar, Saberi and Scaglione, *Discrete (Binary) Opinion Dynamics with Stubborn Agents* (2011), SSRN 1744113, https://ssrn.com/abstract=1744113.

[3] Acemoglu, Como, Fagnani and Ozdaglar, *Opinion Fluctuations and Disagreement in Social Networks* (2010), arXiv:1009.2653v1, https://arxiv.org/abs/1009.2653.

[4] Mori, Hisakado and Nakayama, *A Voter Model on Networks and Multivariate Beta Distribution* (2018), arXiv:1810.05643v1, https://arxiv.org/abs/1810.05643.

[5] Vendeville, Guedj and Zhou, *Towards Control of Opinion Diversity by Introducing Zealots into a Polarised Social Group* (2020), arXiv:2006.07265v1, https://arxiv.org/abs/2006.07265.
