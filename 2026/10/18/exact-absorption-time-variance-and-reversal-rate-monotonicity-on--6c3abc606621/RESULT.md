# Exact absorption-time variance and reversal-rate monotonicity on persistent rings

## Finding
Let \(V_i=\operatorname{Var}(T\mid X_0=i)\), with an initially fair heading. Every starting site has an **exact** finite absorption-time variance; moreover \(V_i\) grows strictly as the heading-reversal rate increases, including when the initial position is the absorbing site. Write \(b=i(n-i)\) and \(q=1+\lambda\). The common site-zero term is
\[
V_0=\frac{n^2}{\kappa^2}+\frac{n(n-1)+\lambda n(n^2-1)/3}{\kappa q}.
\]
For \(1\le i<n\), define
\[
R_{n,i}(\lambda)=\frac{4\lambda^2n^2b-8\lambda^2b^2+4\lambda^2b+2\lambda n^3-2\lambda n+12\lambda b+3n^2+6n-12b}{12q^2}.
\]
Then \(V_i=V_0+R_{n,i}(\lambda)\). The corresponding means are \(\mathbb E_0T=n/\kappa\) and \(\mathbb E_iT=n/\kappa+(2\lambda b+n)/(2q)\) for nonzero \(i\).

## Assumptions and scope
Fix arbitrary integer \(n\ge3\), reversal intensity \(\lambda\ge0\), killing intensity \(\kappa>0\), and initial site \(i\in\{0,\ldots,n-1\}\). The Markov state is the pair of site and heading \(\sigma\in\{-1,+1\}\). The walker moves one site in the heading direction at exponential rate one, and independently reverses heading at rate \(\lambda\). Killing operates at exponential rate \(\kappa\) only when at site zero. The initial heading is uniform; it is not a quenched random parameter. The expressions include \(\lambda=0\) and permit arbitrary strictly positive \(\kappa\).

## Proof
Let \(H\) denote the first *arrival* at site zero from a nonzero site, with heading-dependent first moments \(f_\pm(i)\) and second moments \(g_\pm(i)\). The backward Poisson systems on \(1\le i<n\) are
\[
qf_+(i)-f_+(i+1)-\lambda f_-(i)=1,\qquad qf_-(i)-f_-(i-1)-\lambda f_+(i)=1,
\]
with incoming boundary values \(f_+(n)=f_-(0)=0\). Their unique solution is
\[
f_+(i)=\frac{(n-i)(\lambda i+1)}q,\qquad f_-(i)=\frac{i(\lambda(n-i)+1)}q.
\]
For the second moments, replace the right-hand sides by \(2f_+(i)\), respectively \(2f_-(i)\), and impose \(g_+(n)=g_-(0)=0\). Direct polynomial substitution gives
\[
\begin{split}
g_+(i)=\frac{n-i}{3q^2}\big(&\lambda^2n^2i+\lambda^2ni^2-\lambda^2i^3+\lambda^2i\\
&+\lambda n^2+4\lambda ni-2\lambda i^2+3\lambda i-\lambda\\
&+3n-3i+3\big),\qquad g_-(i)=g_+(n-i).
\end{split}
\]
The finite transient process reaches site zero almost surely and has finite second moments, so solutions of these absorbing Poisson equations are unique. Averaging the two headings and subtracting the **square of their averaged mean** yields \(\operatorname{Var}(H)=R_{n,i}(\lambda)\); averaging their conditional variances instead would be incorrect.

Starting at site zero, reflection interchanges its two headings, so the site-zero absorption time \(A\) has the same distribution after arrival from either direction. The backward equations at site zero give
\[
\mathbb EA=\frac n\kappa,\qquad \mathbb EA^2=\frac{2n^2}{\kappa^2}+\frac{g_+(1)}\kappa,
\]
where \(g_+(1)=n(n-1)[\lambda(n+1)+3]/[3q]\). Hence \(\operatorname{Var}(A)=V_0\). By the strong Markov property, the remainder following first arrival has the same law \(A\) independent of the earlier hitting history; therefore \(T=H+A\), with independent summands. This proves the mean and variance formulas.

For strict monotonicity, differentiate:
\[
\frac{dV_0}{d\lambda}=\frac{n(n-1)(n-2)}{3\kappa q^2}>0,
\]
while for nonzero \(i\),
\[
\frac{dR_{n,i}}{d\lambda}=\frac{\lambda[4b(n^2-2b)-n^3+n-2b]+[n^3-3n^2-7n+18b]}{6q^3}.
\]
Since \(n-1\le b\le n^2/4\), the first bracket is at least \(n^3-(5/2)n^2+n>0\), and the second is at least \(n^3-3n^2+11n-18>0\), for every \(n\ge3\). This proves strict increase everywhere, including at \(\lambda=0\).

## Verification
The standalone `verify.py` independently builds the transient \(2n\)-state generator and solves its first- and second-moment linear systems. For \(3\le n\le40\), each of four reversal intensities and each starting site, it compares direct numerical values with the two closed formulas (a total of 3,268 site-parameter checks). The test uses \(\kappa=1.7\). Symbolic first/second-moment Poisson relations and the site-zero boundary formulas were separately checked algebraically. The proof above establishes all parameters, not just this finite test range.

## Relationship to prior work
Chupeau, Bénichou and Voituriez (2014, arXiv:1406.1687) derive periodic persistent-walk **first-hitting means** and mean cover times in a discrete-time persistence model. These mean calculations are credited: the claim here is the explicit continuous-time finite-rate-sink *variance* and its global strict reversal-rate monotonicity. Mercado-Vásquez and Boyer (2021, arXiv:2102.11787) study first-passage fluctuations for a continuum run-and-tumble particle with a stochastically gated absorbing target in a reflecting interval; different state dynamics and boundary geometry prevent their statements from implying this theorem. General first-passage resolvent methods can in principle produce moments by matrix inversion, but they do not by themselves give the displayed formulas or strict all-size inequality.

## Limitations
The initial heading is fair; heading-resolved variance is different. All jump rates are homogeneous and the ring has precisely one partially absorbing site. The theorem does not concern diffusive continuum limits, multiple traps, spatial disorder, or complete stochastic ordering in reversal rate. Previously unexamined sources may contain equivalent formulas; this is a same-method scientific review, not independent bibliographic certification.

## References
- Chupeau, M., Bénichou, O., and Voituriez, R., *Mean cover time of one-dimensional persistent random walks*, arXiv:1406.1687 (first posted 2014-06-06), https://arxiv.org/abs/1406.1687.
- Mercado-Vásquez, G. and Boyer, D., *First passage time of a run-and-tumble particle with a stochastically gated target*, arXiv:2102.11787 (2021), https://arxiv.org/abs/2102.11787.
- Angelani, L., Di Leonardo, R. and Paoluzzi, M., continuum run-and-tumble first-passage analysis, arXiv:1506.08046 (2015), https://arxiv.org/abs/1506.08046 (abstract considered; full text not compared).
