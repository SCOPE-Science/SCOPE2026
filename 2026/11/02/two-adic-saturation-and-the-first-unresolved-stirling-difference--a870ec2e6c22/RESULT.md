# Two-adic saturation and the first unresolved Stirling-difference index

## Finding

Let \(S(N,k)\) be a Stirling number of the second kind and \(\nu_2\) the two-adic valuation of a nonzero integer. For all integers \(n\ge10\) and \(a>b\ge1\), set
\[
D=S(a2^n,15)-S(b2^n,15),\quad r=\nu_2(a-b),\quad T=b2^n-n-6.
\]
Then
\[
\nu_2(D)=\begin{cases}
n+r+1,&r<T,\\
b2^n-5,&r>T,\\
\text{at least }b2^n-4,&r=T.
\end{cases}
\]
In particular, for each *fixed* positive pair \(a>b\), \(\nu_2(D)=n+1+\nu_2(a-b)\) for all sufficiently large \(n\). The threshold \(T\) also explains why that asymptotic formula does not hold uniformly over pairs depending on \(n\).

## Assumptions and scope

All variables \(a,b,n\) are ordinary positive integers with \(a>b\) and \(n\ge10\); \(k=15\) is fixed. The exponent \(2^n\) is an integer exponent, not a formal variable. The valuation is finite in either strict-inequality branch. The theorem gives a lower bound rather than an exact formula when \(r=T\). All modular calculations below are in the integers. No unstated asymptotic approximation is used.

## Proof

Write \(N=2^n\), \(d=a-b\), and \(c_j=(-1)^{15-j}\binom{15}{j}\). The standard explicit Stirling identity gives
\[
15!D=\sum_{j=1}^{15}c_j(j^{aN}-j^{bN})=:O+E,
\]
where \(O\) contains odd \(j\) and \(E\) contains even \(j\). Since \(\nu_2(15!)=11\), it suffices to determine the valuations of \(O\) and \(E\).

**Odd-base coefficient certificate.** For odd \(j\), set \(x_{j,n}=j^{2^n}-1\), \(q_{j,n}=x_{j,n}/2^n\). The elementary factorization of \(j^{2^n}-1\) (or the lifting-the-exponent identity) gives \(\nu_2(x_{j,n})\ge n+2\), hence \(\nu_2(q_{j,n})\ge2\). Squaring yields the *exact* recurrence
\[
q_{j,n+1}=q_{j,n}+2^{n-1}q_{j,n}^{2}.
\]
For \(n\ge10\), successive terms are therefore congruent modulo \(2^{13}\). Thus
\[
Q_n:=\sum_{\substack{1\le j\le15\\ j\ \mathrm{odd}}}\binom{15}{j}q_{j,n}\equiv Q_{10}\pmod{8192}.
\]
A finite modular certificate computes \(q_{j,10}\pmod{8192}\) for \(j=1,3,5,7,9,11,13,15\) as
\[
0,2292,1660,1496,4584,5420,4548,3952.
\]
Multiplying respectively by \(15,455,3003,6435,5005,1365,105,1\) and summing gives
\[
Q_{10}\equiv4096\pmod{8192},\qquad \nu_2(Q_n)=12\quad(n\ge10).
\]
All eight residues follow simply by calculating \((j^{1024}\bmod2^{23}-1)/1024\). This bounded exact computation is independently reproduced by `verify.py`; the recurrence proves its propagation to **every** \(n\ge10\).

**Odd-part valuation.** For \(t\ge1\), set \(M_t=\sum_{j\ \mathrm{odd}}\binom{15}{j}x_{j,n}^t\). Then \(\nu_2(M_t)\ge t(n+2)\), while \(M_1=2^nQ_n\) has valuation exactly \(n+12\). The ordinary binomial expansion gives
\[
O=\sum_{t\ge1}\Bigl(\binom{a}{t}-\binom{b}{t}\Bigr)M_t,
\]
with finitely many nonzero terms (and \(\binom{u}{t}=0\) when \(t>u\)). For \(t\ge1\), Vandermonde's identity and \(h\binom{d}{h}=d\binom{d-1}{h-1}\) imply
\[
\nu_2\left(\binom{a}{t}-\binom{b}{t}\right)
\ge\nu_2(d)-\lfloor\log_2t\rfloor.
\]
For \(n\ge10\) and every \(t\ge2\),
\[
t(n+2)-\lfloor\log_2t\rfloor\ge n+13.
\]
Therefore all terms with \(t\ge2\) have valuation at least \(n+r+13\), while the \(t=1\) term \(dM_1\) has valuation exactly \(n+r+12\). Hence \(\nu_2(O)=n+r+12\).

**Even-part valuation.** Among the even bases, \(2,6,10,14\) have exactly one factor of two. Their binomial coefficients sum to
\[
\binom{15}{2}+\binom{15}{6}+\binom{15}{10}+\binom{15}{14}=8128=2^6\cdot127.
\]
For each such \(j\), \((j/2)^{bN}\equiv1\pmod{128}\), and \(1-j^{dN}\equiv1\pmod{128}\). The remaining even bases \(4,8,12\) have \(\nu_2(j)\ge2\), hence contribute zero modulo \(2^{bN+7}\). As \(c_j=-\binom{15}{j}\) for even \(j\), we obtain
\[
E/2^{bN}\equiv8128\equiv64\pmod{128},\qquad \nu_2(E)=bN+6.
\]

**Comparison.** Dividing by \(15!\), the odd part has valuation \(n+r+1\) and the even part has valuation \(bN-5\). If these are unequal, the valuation of their sum is their minimum. They coincide exactly when \(r=bN-n-6=T\), in which case cancellation increases the valuation by at least one. This proves all branches. Since \(b2^n-n-6\to\infty\) for fixed \(b\), the first branch eventually holds for every fixed pair \(a>b\). \(\square\)

## Verification

Run `python3 verify.py` with Python 3 and no third-party packages. It recomputes the eight-term modular certificate, the even binomial coefficient sum, 165 complete modular Stirling-difference tests (including very large \(a-b\) in both strict branches and at the collision boundary), and three independent recurrence checks for the Stirling values. The exact output is `VERIFY_OK coefficient_residue=4096 even_binomial_sum=8128 cases= 165 independent_recurrence_pairs= 3`. Modular tests are finite checks; the general statement follows from the proof above.

## Relationship to prior work

Lengyel's 2009 work formulated a general two-adic valuation prediction for differences of Stirling numbers at multiples of powers of two. Zhao, Zhao, and Hong (2014, arXiv:1407.8443) prove the step-doubling conjecture for \(2^m-1\) but explicitly leave their broader arbitrary-\(a,b\) difference prediction open when the fixed index is at least \(15\); their Theorem 1.2 treats indices \(3\) and \(7\). The present theorem proves the **first remaining fixed index** \(15\) in the stable regime and additionally describes an exact finite-level saturation branch. Adelberg (2019, arXiv:1912.01090) gives broad pointwise valuation estimates and a different simultaneous-scaling asymptotic; those statements do not evaluate this difference. The novelty claim is limited to the displayed valuation law, not to the standard Stirling formula, elementary two-adic identities, or earlier special-index results.

## Limitations

The restriction \(n\ge10\) is sufficient, not claimed optimal. On the collision boundary \(r=T\) only a lower bound is established. No formula for fixed indices \(31\) or larger is proved. The theorem does not assert a uniform stable valuation for arbitrary rapidly varying pairs \(a,b\), and it does not imply independent expert verification or publication priority. Undiscovered equivalent earlier results remain a possible literature risk.

## References

- T. Lengyel, *On the 2-adic order of Stirling numbers of the second kind and their differences*, DMTCS Proceedings AK (2009), DOI: 10.46298/dmtcs.2694. Public bibliographic record: https://dmtcs.episciences.org/en/articles/2694
- W. Zhao, J. Zhao, S. Hong, *The 2-adic valuations of differences of Stirling numbers of the second kind*, arXiv:1407.8443 (first public version 2014-07-31). https://arxiv.org/abs/1407.8443
- J. Zhao, S. Hong, W. Zhao, *Divisibility by 2 of Stirling numbers of the second kind and their differences*, arXiv:1209.6284 (2012). https://arxiv.org/abs/1209.6284
- A. Adelberg, *The 2-Adic Analysis of Stirling Numbers of the Second Kind via Higher Order Bernoulli Numbers and Polynomials*, arXiv:1912.01090 (2019). https://arxiv.org/html/1912.01090v1
