# Period spectra and unique reconstruction of binary words with exactly two markers

## Finding

For every integer \(n\ge2\), consider the family \(\mathcal W_n\) of length-\(n\) binary words containing exactly two ones. The *positive period profile* of \(w=w_0\cdots w_{n-1}\) is
\[\mathcal P^+(w)=\{s\in\{1,\ldots,n-1\}: w_t=w_{t+s}\text{ for every }0\le t<n-s\}.\]

**Structural formula.** If the two ones occur at positions \(0\le i<j<n\), set \(p=j-i\) and \(m=\max\{n-i,j+1\}\). Then
\[\mathcal P^+(w)=\{m,\ldots,n-1\}\cup\begin{cases}\{p\},& i<p\text{ and }i+2p\ge n,\\\varnothing,&\text{otherwise.}\end{cases}\]
The interval \(\{m,\ldots,n-1\}\) is empty when \(m=n\).

**Complete profile count.** Write \(K(n)=|\{\mathcal P^+(w):w\in\mathcal W_n\}|\). Then \(K(2)=1\), \(K(3)=2\), and for all \(n\ge4\),
\[K(n)=\left\lfloor\frac n2\right\rfloor-1+\sum_{p=\lfloor n/3\rfloor+1}^{n-1}\left\lceil\frac{\min(n-p,3p-n)}2\right\rceil.\]
This is the quadratic quasipolynomial
\[K(n)=\frac{n^2+8n}{12}-c_{n\bmod6},\quad(c_0,c_1,c_2,c_3,c_4,c_5)=\left(1,\frac74,\frac23,\frac74,1,\frac{17}{12}\right).\]

**Uniquely reconstructible profiles.** Let \(U(n)\) count period profiles attained by exactly one member of \(\mathcal W_n\). For every \(n\ge4\),
\[U(n)=\#\{p:\lfloor n/3\rfloor<p\le n-2,\ p\not\equiv n\pmod2\}+\mathbf 1_{\{n\ge6\text{ and }n\text{ even}\}}.\]
In particular \(K(n)\sim n^2/12\) and \(K(n)/\binom n2\to1/6\).

## Assumptions and scope

Positions are indexed from zero. A positive period \(s\) requires equality only at the \(n-s\) overlapping pairs, not equality after wrapping around the endpoints; the trivial period zero is omitted. Words are labeled, not considered modulo reversal. The weight is exactly two, and \(n\ge2\).

## Proof

**1. Two-one period lemma.** If \(s\) is a period of \(w\), every residue-class chain under steps of length \(s\) is constant. With exactly two ones, a chain containing a one can therefore be either a singleton or one chain of exactly two ones. If both marked positions lie in singleton chains, their indices must be at least \(n-s\) and strictly below \(s\). This is equivalent to \(s\ge\max(n-i,j+1)=m\). Otherwise the two ones must comprise the full same two-element chain. This forces \(s=p=j-i\) and requires the predecessor \(i-p\) to be negative and the successor \(i+2p\) to be outside the word. These conditions are exactly \(i<p\) and \(i+2p\ge n\). This proves the structural formula in both directions, including its endpoint cases.

**2. Pure terminal intervals.** Since \(j\ge i+1\), \(m\ge\lceil(n+2)/2\rceil\). Conversely every \(m\) from \(\lceil(n+2)/2\rceil\) to \(n\) can be realized by the adjacent markers \(i=n-m\) and \(j=n-m+1\); for \(n\ge4\) these are not exceptional. Thus exactly \(\lfloor n/2\rfloor\) pure suffix profiles occur, with \(m=n\) giving the empty profile.

**3. Additional exceptional periods.** Fix \(p\). An exceptional pair exists precisely when
\[L_p=\max(0,n-2p)\le i\le H_p=\min(p-1,n-p-1).\]
The interval is nonempty if and only if \(p\ge\lfloor n/3\rfloor+1\). It has
\[R_p=H_p-L_p+1=\min(n-p,3p-n)\]
integer starting positions. Under reflection \(i\mapsto n-p-1-i\), the two quantities \(n-i\) and \(i+p+1\) exchange, so the corresponding threshold \(m=\max(n-i,i+p+1)\) assumes exactly \(\lceil R_p/2\rceil\) values: each is repeated twice except possibly the central one. For \(p\le n-2\), \(m\ge p+2\), so the exceptional profile has an isolated smallest period \(p\) and cannot coincide with any pure suffix profile or with any exceptional profile for a different \(p\). For \(p=n-1\), the sole exceptional pair \((0,n-1)\) gives the profile \(\{n-1\}\), already attained by a pure suffix profile. Subtracting this single overlap yields
\[K(n)=\left\lfloor\frac n2\right\rfloor-1+\sum_{p=\lfloor n/3\rfloor+1}^{n-1}\left\lceil\frac{R_p}2\right\rceil.\]
The cases \(n=2,3\) are checked directly.

**4. Quasipolynomial evaluation.** Set \(a=\lfloor n/3\rfloor\), \(b=\lfloor n/2\rfloor\), \(L=b-a\), \(s=n-3a\), and \(M=\lceil n/2\rceil-1\). The sum in step 3 splits into
\[\sum_{t=1}^{L}\left\lceil\frac{3t-s}{2}\right\rceil+\sum_{u=1}^{M}\left\lceil\frac u2\right\rceil.\]
Its first term is \(3L(L+1)/4-sL/2+\delta/2\), where \(\delta=\lceil L/2\rceil\) for even \(s\) and \(\delta=\lfloor L/2\rfloor\) for odd \(s\). Its second term is \(\lfloor(M+1)^2/4\rfloor\). Substituting \(n=6k+r\), \(0\le r<6\), gives the six corrections in the finding, including the integral boundary cases.

**5. Singleton reconstruction classes.** For exceptional \(p\le n-2\), exactly one threshold \(m\) occurs only when \(R_p\) is odd, because otherwise every \(m\) arises for two reflected positions. Since \(R_p\equiv p-n\pmod2\), these singleton classes correspond to \(p\not\equiv n\pmod2\). Exceptional \(p=n-1\) is excluded because its profile also occurs among pure suffixes. Of the pure suffix profiles, only the smallest feasible threshold can be singleton, and only when \(n\) is even; the corresponding unique pair is \((n/2-1,n/2)\). At \(n=4\), its profile also arises from exceptional markers at the two endpoints, whereas for even \(n\ge6\) no such duplication occurs. The remaining ordinary thresholds have at least two realizing marker pairs. This proves the stated formula for \(U(n)\).

## Verification

Run the included standalone Python program with `python verify.py`. It independently computes periods using bit comparisons, not the structural formula, for every one of the \(\binom n2\) two-one words at every length \(2\le n\le100\). It checks the six residue-class formula and singleton-profile count at those lengths. Deterministic random tests compare direct periods with the formula at six larger lengths up to \(1000\). Passing tests support the explicit calculations but do not establish the infinite theorem independently of the proof.

## Relationship to prior work

Rivals, Sweering, and Wang (2022 preprint; ICALP 2023) establish global asymptotics for the number of realizable period sets over all words. Rivals and Rahmann (2003) develop general algorithms and combinatorial recurrences for period sets; they do not in their inspected statements give the fixed-weight-two period-profile count, its periodic correction, or the singleton count. Rivals (2024) studies incremental computation and unrestricted period-set enumeration. The present result instead conditions on the binary word having exactly two ones and distinguishes profiles according to reconstructibility within that class. It does not follow by substituting the total unrestricted period-set count into the fixed-weight problem.

## Limitations

The theorem does not count period sets at weight three or higher, does not describe cyclic periods, and does not assert novelty relative to inaccessible or unindexed papers. The fixed-weight-two reconstruction model is a strict subproblem of general period-set enumeration. Computational verification ends at the stated ranges; proofs of the universal statements are combinatorial.

## References

1. E. Rivals, M. Sweering, and P. Wang, *Convergence of the number of period sets in strings*, arXiv:2209.08926, initial public preprint 2022-09-19; ICALP 2023, doi:10.4230/LIPIcs.ICALP.2023.100.
2. E. Rivals and S. Rahmann, *Combinatorics of periods in strings*, Journal of Combinatorial Theory, Series A (2003).
3. E. Rivals, *Incremental computation of the set of period sets*, arXiv:2410.12077 (2024-10-15), later contextual research.
