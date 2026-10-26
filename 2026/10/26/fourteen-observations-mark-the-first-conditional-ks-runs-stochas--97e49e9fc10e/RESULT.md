# Fourteen observations mark the first conditional KS–runs stochastic-order reversal

## Finding

Two classical distribution-free two-sample statistics need not be stochastically aligned when one is conditioned on the other. Put \(a\) plus and \(b\) minus symbols in uniformly random order, with \(a,b\ge1\). Write \(R\) for the number of maximal monochromatic runs. For the prefix after \(t\) symbols, let \(i_t\) and \(j_t\) be its plus and minus counts, and define the two-sided two-sample Kolmogorov–Smirnov statistic
\[
D_{a,b}=\max_{0\le t\le a+b}\left|\frac{i_t}{a}-\frac{j_t}{b}\right|.
\]

**Sharp finite onset.** For every pair of positive integers \(a,b\) with \(a+b\le13\), the conditional law of \(D_{a,b}\) given \(R=r\) is stochastically nonincreasing as \(r\) increases: for all attainable consecutive run counts and all real \(u\),
\[
\Pr(D_{a,b}\ge u\mid R=r)\ge\Pr(D_{a,b}\ge u\mid R=r+1).
\]
The assertion fails for the first time at total size \(a+b=14\): for \((a,b)=(5,9)\), \(r=3\) and \(u=4/5\),
\[
\Pr(D_{5,9}\ge4/5\mid R=3)=\frac13
<\frac{11}{32}=\Pr(D_{5,9}\ge4/5\mid R=4),
\]
a positive reversal of \(1/96\). Up to exchange of the sample labels, the pair \((5,9)\) is the only failing size pair at total size fourteen (although other thresholds for that pair may exist).

**Unbounded family.** For every integer \(a\ge5\), put \(b=2a-1\) and \(u=(a-1)/a\). Then
\[
\Pr(D_{a,b}\ge u\mid R=3)=\frac{4}{3(a-1)},\qquad
\Pr(D_{a,b}\ge u\mid R=4)=\frac{3a-4}{2(a-1)^2},
\]
with the exact strictly positive difference
\[
\Pr(D_{a,b}\ge u\mid R=4)-\Pr(D_{a,b}\ge u\mid R=3)
=\frac{a-4}{6(a-1)^2}>0.
\]
Thus the obstruction is structural and persists for arbitrarily large unbalanced samples.

## Assumptions and scope

The pooled ordering of two independent continuous samples under the common-distribution null is uniform among all \(\binom{a+b}{a}\) binary words containing \(a\) plus symbols and \(b\) minus symbols. No ties occur. The run count is the number of consecutive maximal same-symbol blocks, so \(2\le R\le2\min(a,b)+1\) where attainable; boundary degeneracies are handled by the direct definition. Stochastic ordering refers to all tail thresholds, not solely expectations. Define an integer-scaled walk height \(H_t=bi_t-aj_t\) and maximum \(K=\max_t|H_t|\); then \(K=abD_{a,b}\).

## Proof

### Exact finite bound through thirteen observations

For each \((a,b)\), every possible word is described by its subset of plus positions. The attached standalone checker enumerates all such subsets for \(a+b\le14\). It independently constructs the same exact joint counts by the following dynamic recurrence: at a state with \(i\) plus signs and \(j\) minus signs already placed, last-symbol type \(\ell\), run count \(r\), and integer maximum \(M\), adjoining a plus sign (if \(i<a\)) changes the height to \(b(i+1)-aj\), updates the maximum to \(\max(M,|b(i+1)-aj|)\), and adds one run precisely if the new symbol differs from \(\ell\). The analogous minus transition changes height to \(bi-a(j+1)\). Start with the empty prefix, zero runs and zero maximum. All state multiplicities are integers, and summing terminal states yields the exact joint table \(A_{a,b}(r,k)=\#\{w:R(w)=r,K(w)=k\}\). Both algorithms produce identical tables for every inspected pair.

For every pair of adjacent attainable run counts, the checker computes all tail counts \(T_r(t)=\sum_{k\ge t}A_{a,b}(r,k)\) and denominators \(N_r=\sum_kA_{a,b}(r,k)\) exactly. It compares the cross products \(T_r(t)N_{r+1}\) and \(T_{r+1}(t)N_r\) at every distinct attainable \(k\); these exhaust real thresholds because tail probabilities are constant between consecutive support values. Labels can be exchanged without changing \(D\) or \(R\), so only \(a\le b\) is needed. The exhaustive finite certificate covers every positive \(a,b\) with \(a+b\le13\), and also all size pairs at \(a+b=14\). It yields no violation through thirteen and identifies \((a,b)=(5,9)\) as the sole failing size pair at fourteen. This is a finite exhaustive certificate, not an induction or a theorem about all sample sizes.

### An analytic family of counterexamples

Fix an integer \(a\ge5\), set \(b=2a-1\), and write \(T=b(a-1)\), so \(K\ge T\) is exactly \(D_{a,b}\ge(a-1)/a\).

A three-run word has one of the two forms \(+^i-^b+^{a-i}\), with \(1\le i<a\), or \(-^j+^a-^{b-j}\), with \(1\le j<b\). Their respective integer maxima are \(b\max(i,a-i)\) and \(a\max(j,b-j)\). For the first orientation the threshold is reached exactly at \(i=1\) or \(i=a-1\). For the second orientation, since \(b=2a-1\), the inequality \(a\max(j,b-j)\ge b(a-1)\) holds exactly at \(j=1\) or \(j=b-1\). Consequently exactly four of the \(a+b-2=3(a-1)\) three-run words reach the threshold. This proves \(P_3=4/[3(a-1)]\).

A four-run word starting with plus is uniquely \(+^i-^j+^{a-i}-^{b-j}\), with \(1\le i<a\), \(1\le j<b\). Its nonzero run-boundary heights are \(bi\), \(bi-aj\), and \(a(b-j)\). The middle height never has absolute value \(T\) or greater: \(bi-aj<T\), and \(aj-bi\le a(b-1)-b<T\). The first height reaches \(T\) precisely when \(i=a-1\). The third height reaches \(T\) precisely when \(j=1\); indeed \(a(b-j)\ge b(a-1)\) is equivalent to \(aj\le b\), and \(b/a<2\). Taking the union yields \((b-1)+(a-1)-1=3a-4\) successful four-run words starting with plus.

Reversing a word preserves both the run count and the maximum absolute height, because the path ends at height zero. Thus the same number of successful words start with minus. There are exactly \(2(a-1)(b-1)=4(a-1)^2\) four-run words, so \(P_4=2(3a-4)/[4(a-1)^2]=(3a-4)/[2(a-1)^2]\). Subtraction yields the claimed strictly positive difference \((a-4)/[6(a-1)^2]\).

For \(a=5\) the two denominators are \(12\) and \(64\), and the successful counts are \(4\) and \(22\), proving the concrete reversal without reliance on a computer.

## Verification

Run the self-contained Python 3 checker \(\texttt{verify_ks_runs.py}\), provided with this result. It uses only the standard library; enumeration and independent state propagation are exact integer computations. It cross-checks all \(49\) unordered positive size pairs with total size at most fourteen, independently checks the analytical three/four-run formulas for \(a=5,\ldots,44\), verifies the minimality through thirteen, and reports the unique failing size pair at fourteen. Direct enumeration at finite sizes does not establish the infinite family: the latter is proved algebraically above. The checker also confirms all run-count denominators and uses integer cross multiplication, avoiding floating-point thresholds.

## Relationship to prior work

The two-sample Kolmogorov–Smirnov and Wald–Wolfowitz statistics are classical. Vellore (1972) studied the joint laws of Kolmogorov–Smirnov statistics and runs, with later surveys describing the equal-sample case. Saran and Sen (1978) and Saran (1995) discuss joint rank statistics and runs; Saran (1995), whose accessible full text was inspected, emphasizes crossing counts, visits, sojourns, and arbitrary sample sizes. The lattice-path treatment by Krattenthaler and Mohanty discusses the two statistics together and earlier joint enumerations. These results supply general counting context and in some cases formulas capable of deriving individual probabilities; the specific conditional stochastic-order question, its first unequal-size failure at fourteen, and the unbounded sign-reversal family were not identified among the inspected statements. This is a qualified comparison, not a proof of bibliographic uniqueness. Some older complete primary texts, especially Saran–Sen (1978) and Vellore (1972), remained inaccessible and present an explicit priority risk.

## Limitations

The finite-size cutoff is a finite exhaustive statement whose validity depends on correct implementation of the fully stated enumeration recurrence and its independent brute-force cross-check. No monotonicity assertion is made for all larger sample sizes. The counterexamples involve the two-sided, correctly normalized two-sample statistic, not an unweighted signed-walk maximum. No claim is made about one-sided Kolmogorov–Smirnov statistics, other conditioning events, or power under alternatives. Historical priority requires further scrutiny of inaccessible older joint-distribution papers; independent audit has not been performed.

## References

1. Clifford E. Lunneborg, *Runs Test*, Encyclopedia of Statistics in Behavioral Science, DOI: 10.1002/0470013192.bsa576, first published 15 October 2005.
2. Jagdish Saran, *Joint distributions based on the number of runs and some other two-sample rank order statistics for arbitrary sample sizes*, Journal of Statistical Planning and Inference 47 (1995), 257–275, DOI: 10.1016/0378-3758(94)00138-L.
3. Jagdish Saran and K. Sen, *On the distributions of Kolmogorov–Smirnov statistics, sojourns, intersections and runs*, Metron 36 (1978), 65–78. Full text not obtained.
4. S. Vellore, *Joint distributions of Kolmogorov–Smirnov statistics and runs*, Studia Scientiarum Mathematicarum Hungarica 7 (1972), 155–165. Full text not obtained.
5. C. Krattenthaler and S. G. Mohanty, *Lattice Path Combinatorics—Applications to Probability and Statistics*, survey PDF, sections on two-sample tests and run counts.
6. C. Krattenthaler, *Lattice Path Enumeration*, arXiv:1503.05930 (first submitted 19 March 2015), background on lattice-path counting.
