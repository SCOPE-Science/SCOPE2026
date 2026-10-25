# Entropy-phase and exact periodic-point spectra of two-neighbor modular spacing shifts

## Finding

For each integer \(m\ge3\), consider the two-sided binary spacing shift \(X_m\) in which any two positions carrying 1 must have a distance **not** congruent to \(\pm1\) or \(\pm2\) modulo \(m\). Let \(\sigma\) denote the left shift and \(k=\lfloor m/3\rfloor\). Its topological entropy is
\[
h_{\mathrm{top}}(X_m)=\frac{k}{m}\log 2.
\]
There are exactly
\[
N_m=\begin{cases}1,&m\equiv0,1\pmod3,\\1+\lfloor k/2\rfloor,&m=3k+2\end{cases}
\]
ergodic measures of maximal entropy. Each comes from a cyclic orbit of maximum independent sets of the second power of the length-\(m\) cycle, by retaining fair independent bits on allowed residue classes and placing zero elsewhere. The measurable eigenvalue group for each measure is exactly the group of \(d\)-th roots of unity. The phase period is \(d=3\) for \(m=3k\), and \(d=m\) for \(m=3k+1\). For \(m=3k+2\), all phases have period \(m\), except that if \(k\) is even, precisely one maximal-entropy measure has phase period \(m/2\). Thus the number of ergodic entropy-maximizers is unbounded as \(m\) ranges over integers congruent to 2 modulo 3.

For every \(n\ge1\), put \(g=\gcd(n,m)\). The exact periodic-point count is
\[
|\operatorname{Fix}(\sigma^n)|=1+\sum_{j=1}^{\lfloor g/3\rfloor}\frac gj\binom{g-2j-1}{j-1}\bigl(2^{n/g}-1\bigr)^j.
\]
An empty sum is zero. In particular, a positive-entropy shift in this family has only the all-zero periodic point at any period relatively prime to \(m\), and even at every period with \(g\le2\).

## Assumptions and scope

The space is \(\{0,1\}^{\mathbb Z}\) with the product topology, and the shift is \((\sigma x)_i=x_{i+1}\). Differences are between distinct integer positions, so multiples of \(m\) are allowed. Only \(m\ge3\) is asserted, avoiding a looped residue constraint. The entropy uses natural logarithms; measurable eigenvalues are those of the Koopman operator on the complex \(L^2\) space of the specified ergodic measure. Periodic points are points fixed by an iterate, not points of least period equal to that iterate.

## Proof

**1. Residue-mask reduction.** For \(x\in X_m\), form \(S(x)=\{i\bmod m:x_i=1\}\). The spacing condition is equivalent to \(S(x)\) being an independent set of the graph \(C_m^2\), with edges at circular distances 1 and 2. Conversely, fixing any such set \(S\), all binary sequences supported at integer sites whose residues belong to \(S\) lie in \(X_m\). Consequently the entire shift is the finite union of these periodic-template subshifts. Under \(\sigma\), the actual residue set rotates. A Borel invariant ergodic probability measure has its residue set in one finite rotation orbit almost surely.

**2. Entropy and maximizing measures.** If a mask \(S\) has \(j\) residues, its template subsystem has \(j\) free coordinates per \(m\) symbols. The union of its cyclic rotations has entropy \((j/m)\log2\). For a mask with rotation period \(d\mid m\), the \(d\)-th iterate on a fixed phase is a full shift on \(2^{jd/m}\) symbols; the exponent is an integer because the mask is periodic with period \(d\). This full shift has a unique maximal-entropy measure, the uniform Bernoulli measure. Uniformly distributing its phase over the \(d\) translates gives an ergodic invariant measure with entropy \((j/m)\log2\). Any other invariant measure carried by that orbit has no larger entropy, with equality only for this one measure. Since the union over mask orbits is finite, every global maximal-entropy measure is a convex combination of the maximizers on orbits of masks of maximum size. For the particular ergodic maximizer, almost every allowed residue class contains infinitely many 1s, hence its mask phase is recoverable from the observed sequence. Under the \(d\)-th iterate, each phase is a Bernoulli shift, which has no nontrivial measurable eigenvalues. Therefore any eigenvalue of \(\sigma\) obeys \(\lambda^d=1\), and every \(d\)-th root occurs on functions of the cyclic phase. This determines the complete point spectrum.

**3. Sharp cyclic-gap classification.** Suppose a nonempty mask has \(j\) occupied residues. Listing them in circular order gives \(j\) positive cyclic gaps, each at least 3, summing to \(m\). Hence \(j\le\lfloor m/3\rfloor=k\), and equality is attained. When \(m=3k\), all \(k\) gaps equal 3, giving one rotation orbit of phase period 3. When \(m=3k+1\), exactly one gap is 4 and all others are 3, giving one orbit of phase period \(m\). When \(m=3k+2\), either one gap is 5 or two gaps are 4, with all remaining gaps 3. The former yields one orbit. The latter occurs only if \(k\ge2\); its two marked gaps are classified up to cyclic rotation by their cyclic separation \(j\), identified with \(k-j\), yielding exactly \(\lfloor k/2\rfloor\) orbits. A nontrivial period of a gap list with just two marked positions is possible only when \(k\) is even and they are opposite; this gives exactly one orbit with physical phase period \(m/2\). Every other mask in this case has period \(m\). This proves the entropy, the entire maximizing-measure census, and its eigenvalue spectrum.

**4. Exact counts for every iterate.** Fix \(n\ge1\), let \(g=\gcd(n,m)\) and \(s=n/g\). A point fixed by \(\sigma^n\) is a repetition of an \(n\)-bit word. If one coordinate in an index class modulo \(g\) carries 1, its periodic repetitions sweep all residues modulo \(m\) in that class. Thus, the set of index classes modulo \(g\) that contain any 1 must be 2-separated on the length-\(g\) circle. For \(g=1,2\), every nonempty class hits a forbidden congruence after repetitions, so there is only the zero point. For \(g\ge3\), a selected class admits \(2^s-1\) nonempty fillings of the \(s\) positions it occupies in one \(n\)-block. The number of 2-separated size-\(j\) subsets of the length-\(g\) circle is
\[
\frac gj\binom{g-2j-1}{j-1}.
\]
Indeed the \(j\) cyclic gaps are at least 3, so after subtracting 3 they are a weak composition of \(g-3j\) into \(j\) parts; there are \(\binom{g-2j-1}{j-1}\) such compositions, \(g\) choices of starting position, and each subset was counted \(j\) times. Multiplying by the nonempty filling count and summing over \(j\) proves the displayed formula. It is exact for all \(m\) and \(n\), with no asymptotic approximation.

## Verification

The standalone `verify.py` independently enumerates independent masks and rotation orbits for \(3\le m\le16\), checking entropy mask sizes, counts of maximizing measures, and phase periods. For \(3\le m\le12\) and \(1\le n\le12\), it independently enumerates length-\(n\) binary periodic words, tests the forbidden difference congruences over their full joint period, and compares all counts with the exact formula. These finite checks test boundary and small parameter cases; the four analytical steps above establish the unrestricted claims.

## Relationship to prior work

Kwietniak's work on hereditary and spacing shifts establishes general entropy and recurrence criteria but not this all-modulus maximizing-measure, phase-spectrum, and periodic-point classification. Kułaga-Przymus, Lemańczyk and Weiss explicitly study Bernoulli thinnings of periodic templates and exhibit hereditary shifts with multiple maximal-entropy measures; that general mechanism underlies Step 2 and is not claimed as new. White's later cyclic-sieving theorem supplies the broad independent-set counting framework for powers of cycles, covering the combinatorial coefficient in Step 4; its independent-set enumeration is not claimed as a new graph result. The contribution here is the complete dynamical synthesis for the pairwise modular two-neighbor exclusion family, including the exact entropy-maximizer census, exceptional measurable phase spectra, and all-iterate periodic-point function. Banks, Oprocha and Stanley study sofic spacing shifts and transitivity; their abstract was available, but their complete article was not accessible for a definitive priority comparison.

## Limitations

This concerns the specific symmetric forbidden residues \(\pm1,\pm2\) modulo \(m\), and does not classify arbitrary modular forbidden sets, mixing behavior of general spacing shifts, or fine periodic-point asymptotics under perturbations. The general periodic-template and cyclic-sieving ingredients are established earlier; independent historical priority of their particular combination for this shift family is not certified. The unavailable complete 2015 sofic-spacing-shift source remains a relevant originality risk. No independent scientific audit has been performed.

## References

- D. Kwietniak, *Topological entropy and distributional chaos in hereditary shifts with applications to spacing shifts and beta shifts*, arXiv:1111.0190, first posted 2011-11-01; *Discrete and Continuous Dynamical Systems* 33 (2013), 2451–2467.
- J. Kułaga-Przymus, M. Lemańczyk, B. Weiss, *On invariant measures for \(\mathscr B\)-free systems*, arXiv:1406.3745 (2014), especially Section 3.2 on periodic-template hereditary shifts.
- J. A. White, *Cyclic Sieving Phenomenon for Independent sets of graphs*, arXiv:2605.03083 (2026), particularly Theorem 1 and its cyclic powers of cycles examples.
- J. Banks, P. Oprocha, B. Stanley, *Transitive sofic spacing shifts*, *Discrete and Continuous Dynamical Systems* 35 (2015), 4743–4764, DOI:10.3934/dcds.2015.35.4743; full-text comparison unresolved.
