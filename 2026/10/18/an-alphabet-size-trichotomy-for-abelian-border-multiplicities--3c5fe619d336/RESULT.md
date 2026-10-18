# An alphabet-size trichotomy for Abelian-border multiplicities

## Finding

For a finite word, an **Abelian border** of length \(j\) is a nonempty proper prefix whose symbol multiplicity vector equals that of the suffix of length \(j\). Each possible length counts once, regardless of how many permutations identify the prefix and suffix.

Fix an integer alphabet size \(q\ge 2\). Let \(W_n\) be a uniformly sampled length-\(n\) word on \(q\) labeled symbols, and let \(B_{n,q}\) count its distinct proper Abelian-border lengths. Put \(m=\lfloor n/2\rfloor\), and define
\[
p_q(j)=q^{-2j}\sum_{a_1+\cdots+a_q=j}\binom{j}{a_1,\ldots,a_q}^{\!2},\qquad
G_q(z)=\sum_{j\ge0}p_q(j)z^j,\qquad p_q(0)=1.
\]
All sums in the definition of \(p_q(j)\) are over nonnegative integers. The following statements hold.

**Exact finite laws.** For every \(n\ge1\),
\[
\mathbb E B_{n,q}=2\sum_{j=1}^{m}p_q(j)-\mathbf1_{\{2\mid n\}}p_q(m).
\]
The complete distribution at every odd length is specified by the formal power-series identity
\[
\boxed{\displaystyle
\sum_{m\ge0}z^m\mathbb E\bigl[u^{B_{2m+1,q}}\bigr]
=\frac{1}{(1-z)\bigl(u^2+(1-u^2)G_q(z)\bigr)}.}
\]
At every even length the border-count distribution is likewise obtained from the exactly specified coupled random walk in the proof; there is no independence assumption between border lengths.

**Three limiting laws.** Let \(Z\) be standard normal, \(E\) exponential of mean one, and \(J_q\) a geometric random variable supported on \(\{0,1,2,\ldots\}\). For fixed \(q\), as \(n\to\infty\),
\[
\boxed{\begin{array}{ll}
q=2: & B_{n,2}/\sqrt n\ \Longrightarrow\ 2|Z|,\\[2pt]
q=3: & B_{n,3}/\log n\ \Longrightarrow\ \dfrac{3\sqrt3}{2\pi}E,\\[3pt]
q\ge4: & B_{n,q}\ \Longrightarrow\ 2J_q,
\end{array}}
\]
where
\[
\mathbb P(J_q=r)=G_q(1)^{-1}\bigl(1-G_q(1)^{-1}\bigr)^r\quad(r\ge0),
\qquad 1<G_q(1)<\infty\quad(q\ge4).
\]
For \(q\ge4\), the total-variation distance to \(2J_q\) is \(O_q(n^{-(q-3)/2})\). Thus the limiting laws exhibit a sharp transition between square-root growth, logarithmic growth, and a finite geometric law.

In particular, the exact expectation has the asymptotic forms
\[
\mathbb E B_{n,q}=\begin{cases}
2\sqrt{2n/\pi}+O(1),&q=2,\\
\dfrac{3\sqrt3}{2\pi}\log n+O(1),&q=3,\\
2(G_q(1)-1)+O_q\bigl(n^{-(q-3)/2}\bigr),&q\ge4.
\end{cases}
\]
The probability of **no proper Abelian border** has the additional sharp trichotomy
\[
\mathbb P(B_{n,q}=0)=\begin{cases}
\dfrac{\binom{2m}{m}}{4^m},&q=2,\\[6pt]
\dfrac{4\pi}{3\sqrt3\log n}\bigl(1+o(1)\bigr),&q=3,\\[6pt]
G_q(1)^{-1}+o(1),&q\ge4.
\end{cases}
\]
The binary enumerations underlying the first case are known in earlier work; the contribution here is the multialphabet exact renewal distribution and the different limiting regimes, including the ternary exponential law and the finite-alphabet geometric limit.

## Assumptions and scope

The alphabet has \(q\) labeled symbols, each chosen independently with probability \(1/q\). The integer \(q\) is fixed while \(n\) tends to infinity. Abelian equality means equality of all symbol counts, not equality of ordered letters. A border is proper: lengths \(1,\ldots,n-1\) only. The generating-function statement is an identity of formal power series in \(z\), with coefficients polynomial in \(u\). The value \(G_q(1)\) is a convergent positive series only when \(q\ge4\). The assertion does not cover nonuniform letter probabilities or alphabets growing with word length.

## Proof

**1. Exact reduction to returns.** Index the letters of a given word as \(w_1,\ldots,w_n\), and let \(e_i\) be standard basis vectors of \(\mathbb Z^q\). For \(1\le j\le m\), define
\[
S_j=\sum_{i=1}^j(e_{w_i}-e_{w_{n+1-i}}),\qquad S_0=0,
\qquad R_m=\sum_{j=1}^{m}\mathbf1_{\{S_j=0\}}.
\]
A length-\(j\) Abelian border exists exactly when \(S_j=0\). If a border has length \(j>n/2\), cancel its overlapping central portion: it exists exactly when the complementary length \(n-j\) is a border. Therefore
\[
\boxed{\displaystyle B_{n,q}=2R_m-\mathbf1_{\{2\mid n\}}\mathbf1_{\{S_m=0\}}.}\tag{1}
\]
Under the uniform product measure, the disjoint outer letter pairs are independent and uniform. Thus the increments of \(S_j\) are independent copies of \(e_X-e_Y\), for independent uniform letters \(X,Y\). They live in the \((q-1)\)-dimensional integer lattice whose coordinates sum to zero. Its origin-return probability at time \(j\) is exactly \(p_q(j)\), since a return means that the two independent length-\(j\) sampled words have identical histograms. Taking expectations in (1) proves the exact expectation formula.

**2. Renewal identity.** Let \(f_q(j)\) be the probability that \(S_j=0\) for the first positive time at \(j\), and set \(F_q(z)=\sum_{j\ge1}f_q(j)z^j\). The strong Markov property, including possible one-step loops at the origin, gives
\[
G_q(z)=1+F_q(z)G_q(z),\qquad F_q(z)=1-1/G_q(z).
\]
The generating function of probabilities that no positive return has occurred by time \(m\) is \((1-F_q(z))/(1-z)\). A path with exactly \(r\) returns by time \(m\) consists of \(r\) completed first-return excursions and one surviving tail. Hence
\[
\sum_{m\ge0}z^m\mathbb E[v^{R_m}]
=\frac{1-F_q(z)}{(1-z)(1-vF_q(z))}
=\frac{1}{(1-z)\bigl(v+(1-v)G_q(z)\bigr)}.
\]
For an odd length, (1) says \(B_{2m+1,q}=2R_m\); substituting \(v=u^2\) proves the claimed generating function. This derivation also provides an exact coefficientwise algorithm for every fixed \(q\).

**3. Return-kernel asymptotic.** Use the first \(q-1\) coordinates of the increments. For \(\theta\in[-\pi,\pi]^{q-1}\), their characteristic function is
\[
\phi_q(\theta)=\left|\frac{1+\sum_{j=1}^{q-1}e^{\mathrm i\theta_j}}q\right|^2.
\]
Fourier inversion yields \(p_q(k)=(2\pi)^{-(q-1)}\int\phi_q(\theta)^k\,d\theta\). The only point with \(|\phi_q|=1\) on this torus is the origin: equality in the triangle inequality forces all \(q\) complex phases to coincide. Writing \(d=q-1\), near the origin
\[
\phi_q(\theta)=1-\theta^\mathsf T V_q\theta+O_q(\|\theta\|^4),
\qquad V_q=\frac1q I_d-\frac1{q^2}\mathbf1\mathbf1^\mathsf T,
\quad\det V_q=q^{-q}.
\]
The matrix has eigenvalues \(1/q\) with multiplicity \(q-2\) and \(1/q^2\) with multiplicity one. Laplace's method, with an exponentially small complement away from the unique saddle, therefore proves
\[
\boxed{\displaystyle
p_q(k)=\frac{q^{q/2}}{(4\pi k)^{(q-1)/2}}\bigl(1+O_q(k^{-1})\bigr).}\tag{2}
\]
The uniform positive-definiteness of the quadratic form near zero and the even analytic expansion justify the relative error. In particular, write \(c_2=1/\sqrt\pi\) and \(c_3=3\sqrt3/(4\pi)\). Then \(p_2(k)=c_2 k^{-1/2}+O(k^{-3/2})\), \(p_3(k)=c_3 k^{-1}+O(k^{-2})\), and \(\sum_{k\ge0}p_q(k)<\infty\) exactly when \(q\ge4\).

**4. Binary limit law.** For each fixed integer \(r\ge1\), the strong Markov property gives an exact falling-factorial-moment identity
\[
\mathbb E[(R_m)_r]=r!\sum_{\substack{h_1,\ldots,h_r\ge1\\h_1+\cdots+h_r\le m}}\prod_{i=1}^r p_2(h_i).
\]
Rescale the summation region by \(m\). The power bound in (2), truncation near the coordinate hyperplanes, and the Dirichlet integral imply
\[
\frac{\mathbb E[(R_m)_r]}{m^{r/2}}
\longrightarrow r!c_2^r\frac{\Gamma(1/2)^r}{\Gamma(1+r/2)}
=\frac{r!}{\Gamma(1+r/2)}.
\]
Replacing factorial moments by ordinary moments changes only lower-order terms. These are exactly the moments of \(\sqrt2|Z|\), by the gamma duplication formula; the half-normal distribution is moment-determinate. Thus \(R_m/\sqrt m\Longrightarrow\sqrt2|Z|\). Equation (1) and \(m/n\to1/2\) yield \(B_{n,2}/\sqrt n\Longrightarrow 2|Z|\). This recovers, in probabilistic form, information implicit in the known binary finite enumeration.

**5. Ternary limit law.** For any fixed \(r\), the same factorial-moment identity with \(p_3\) holds. Its inner sum is sandwiched between
\[
\left(\sum_{j\le\lfloor m/r\rfloor}p_3(j)\right)^r
\quad\text{and}\quad
\left(\sum_{j\le m}p_3(j)\right)^r.
\]
Both are asymptotic to \((c_3\log m)^r\) by (2). Consequently
\[
\mathbb E\left[(R_m/\log m)^r\right]\longrightarrow r!c_3^r.
\]
These moments determine an exponential variable of mean \(c_3\). The additive central correction in (1) is at most one, giving the ternary limit displayed in the finding.

**6. Transience and the geometric law.** For \(q\ge4\), (2) shows that \(G_q(1)<\infty\). Sending \(z\uparrow1\) in the renewal equation gives a probability of some positive return
\[
f_q=F_q(1)=1-G_q(1)^{-1}<1.
\]
Successive completed return excursions are independent by the strong Markov property; the number \(J_q\) of returns in an infinite path therefore has \(\mathbb P(J_q=r)=(1-f_q)f_q^r\). Coupling a finite outer-pair path to that infinite walk and using (1), disagreement between \(B_{n,q}\) and \(2J_q\) requires a return at some time \(k\ge\lfloor n/2\rfloor\). By a union bound and (2),
\[
\mathbb P(B_{n,q}\ne2J_q)\le\sum_{k\ge\lfloor n/2\rfloor}p_q(k)
=O_q(n^{-(q-3)/2}),
\]
which implies the claimed total-variation bound and limiting distribution. The same return series gives \(\mathbb E J_q=G_q(1)-1\).

**7. Expectations and unbordered probability.** Sum (2) in the exact expectation identity: square-root and logarithmic partial sums give the first two regimes, and summability plus its tail bound gives the third. In every parity, (1) also yields
\[
\mathbb P(B_{n,q}=0)=\mathbb P(R_m=0).
\]
For \(q=2\), the central-binomial identity gives \(G_2(z)=(1-z)^{-1/2}\); the survival generating function in Step 2 becomes \((1-z)^{-1/2}\), so its coefficient is \(\binom{2m}{m}4^{-m}\). For \(q\ge4\), survival decreases to \(1/G_q(1)\). For \(q=3\), (2) gives \(G_3(z)\sim c_3\log(1/(1-z))\) as \(z\uparrow1\). Hence the survival generating function behaves as \(1/(c_3(1-z)\log(1/(1-z)))\). The monotone-density form of the Hardy–Littlewood–Karamata Tauberian theorem applies to the nonincreasing survival probabilities, yielding \(\mathbb P(R_m=0)\sim1/(c_3\log m)\). The stated unbordered limits follow.

## Verification

Run `python3 artifacts/verify.py` from the directory containing this document. Its three independent procedures calculate every Abelian-border count by direct word enumeration, by a separate vector-state dynamic program, and, for odd lengths, by first-return convolution. The script compares all three for alphabets of sizes two, three, and four through word length eight. It also reproduces the published ternary counts of Abelian-unbordered words through word length ten and checks exact rational multinomial return probabilities. The tests ran successfully on the bundled version of the script. They check finite values only; the proofs of (2) and of the limit laws are analytic.

## Relationship to prior work

The 2014 work of Goč, Rampersad, Rigo, and Salimov establishes the fundamental lattice-path mapping for arbitrary alphabets and counts Abelian-**unbordered** words, notably using triangular-lattice paths in the ternary case (Propositions 15–16 and Section 4). That mapping is acknowledged, not claimed as new. Blanchet-Sadri, Chen, and Hawes (2017) determine the **complete finite distribution of the number of borders over a binary alphabet** (Theorem 3); the binary part here is a consistency benchmark, not a new enumeration. Habib, Shamil, and Rahman (2021) count binary Abelian-border **arrays** and discuss the difficulty of extending their array results to larger alphabets; that inverse problem is different from the multiplicity variable studied here.

The contribution isolated here is the exact multialphabet return-count generating function and the alphabet-dependent full limit laws, with their constants, unbordered probabilities, and quantitative geometric convergence. The 2014 result supplies one antecedent (zero borders), but neither its reported counting formulas nor the 2017 binary distribution gives the nonbinary return-multiplicity distribution or the limiting-law trichotomy. A standard stochastic-process interpretation does not by itself supply the constants and complete three-regime statements without the return-kernel analysis performed here.

## Limitations

The theorem concerns uniformly random finite words with fixed alphabet size; it does not give an explicit elementary closed form for \(G_q(1)\) when \(q\ge4\). The nonbinary result remains potentially covered by literature on lattice-walk local times not indexed under Abelian-border terminology, although no equivalent stringological statement was found in the comparisons described in the accompanying review. Convergence in law for fixed alphabet size does not imply a uniform result in growing alphabet size. Finite checks are supplementary and should not be treated as a proof of the infinite statements.

## References

1. D. Goč, N. Rampersad, M. Rigo, and P. Salimov, *On the Number of Abelian Bordered Words (with an Example of Automatic Theorem-Proving)*, International Journal of Foundations of Computer Science **25** (2014), 1097–1110. DOI: `10.1142/S0129054114400267`. Accessible author/PDF version: `https://scispace.com/pdf/on-the-number-of-abelian-bordered-words-with-an-example-of-43gdbru0k3.pdf`.
2. F. Blanchet-Sadri, K. Chen, and K. Hawes, *Dyck Words, Lattice Paths, and Abelian Borders*, Electronic Proceedings in Theoretical Computer Science **252** (2017), 56–70. DOI: `10.4204/EPTCS.252.9`; first public arXiv version: `arXiv:1708.06461` (22 August 2017).
3. M. Habib, M. S. Shamil, and M. S. Rahman, *Counting and Verifying Abelian Border Arrays of Binary Words*, `arXiv:2111.00259v1` (30 October 2021).
4. N. H. Bingham, C. M. Goldie, and J. L. Teugels, *Regular Variation*, Cambridge University Press (1987), for the monotone-density Tauberian principle invoked in the survival asymptotic.
