# Exact fiber law and saturation for triangular residues at every modulus

## Finding
For a positive integer \(m\), define the triangular number \(T(n)=n(n+1)/2\) and its first-block fiber multiplicities
\[M_m(t)=\#\{0\le n<m:T(n)\equiv t\pmod m\},\qquad t\in\mathbb Z/m\mathbb Z.\]
Let \(q=m/2^{\nu_2(m)}\) denote the odd part of \(m\). For an odd prime \(p\), exponent \(e\ge1\), and integer \(D\), define
\[N_{p,e}(D)=\begin{cases}
p^{\lfloor e/2\rfloor},&p^e\mid D,\\
2p^j,&\nu_p(D)=2j<e\text{ and }D/p^{2j}\text{ is a nonzero square modulo }p,\\
0,&\text{otherwise}.
\end{cases}\]
**Exact fiber theorem:** for all \(m\ge1\) and residue classes \(t\pmod m\),
\[\boxed{M_m(t)=\prod_{p^e\parallel q}N_{p,e}(1+8t).}\]
The empty product for \(q=1\) equals one. Thus every residue of a power-of-two modulus occurs exactly once among the first \(m\) triangular numbers, while for any odd \(q\), adjoining an arbitrary factor \(2^a\) lifts each fiber equally to all \(2^a\) residue classes over it.

Writing \(C_{p,e}=1+(p-1)\sum_{j=0}^{\lfloor(e-1)/2\rfloor}p^{e-2j-1}/2\), the image size and saturation are
\[\boxed{\#\{T(n)\bmod m:n\ge0\}=\prod_{p^e\parallel q}C_{p,e},\qquad \sigma(m)=\prod_{p^e\parallel q}\frac{C_{p,e}}{p^e}.}\]
For an odd squarefree \(q\) with exactly \(r\) prime factors, the positive fiber sizes are precisely \(\{1,2,4,\ldots,2^r\}\), both for \(m=q\) and \(m=2q\). Hence adding the prime factor two does not add another level to the fiber-size spectrum, contrary to an unqualified prediction for products of distinct primes.

## Assumptions and scope
All moduli \(m\) are positive integers; the class \(t\) may be any residue, including one not attained. The valuation condition in \(N_{p,e}\) applies to \(D\bmod p^e\), so the zero case is unambiguous. Only odd primes appear in the product. The count \(M_m(t)\) always uses exactly the integers \(0\le n<m\), even when the full triangular sequence has period \(2m\). Nonzero fiber sizes refer to image residues only.

## Proof
**1. Odd local roots.** The identity
\[8T(n)+1=(2n+1)^2\]
shows, when \(q\) is odd, that \(T(n)\equiv t\pmod q\) is equivalent under the bijection \(n\mapsto2n+1\) of \(\mathbb Z/q\mathbb Z\) to \(x^2\equiv 1+8t\pmod q\). For an odd prime power \(p^e\), if \(p^e\mid D\), the solutions are precisely multiples of \(p^{\lceil e/2\rceil}\), giving \(p^{\lfloor e/2\rfloor}\) roots. If \(\nu_p(D)=2j<e\), solutions must have valuation \(j\). Their unit parts satisfy \(y^2\equiv D/p^{2j}\pmod{p^{e-2j}}\). By the simple-root Hensel lifting of nonzero quadratic residues for odd \(p\), this has exactly two unit roots if the residue is a square modulo \(p\), and none otherwise; each root gives \(p^j\) lifts modulo \(p^e\). Odd valuations cannot be square valuations. This proves the local formula. CRT yields the product for all odd \(q\).

**2. Exactly two local solutions at the prime two.** For each \(a\ge1\), \(T(x)\equiv T(y)\pmod{2^a}\) is equivalent to
\[2^{a+1}\mid (x-y)(x+y+1).\]
Exactly one of these two factors is odd. Hence \(x\equiv y\pmod{2^{a+1}}\) or \(x\equiv-y-1\pmod{2^{a+1}}\). These alternatives are distinct, so each represented residue has precisely two roots among all \(2^{a+1}\) possible inputs. Since there are \(2^a\) residue classes, all are represented, each twice. For \(a=0\), the modulus one has one input and one output, consistent with the empty-product convention.

**3. The first-block halving lemma.** For arbitrary \(m\), the full triangular sequence modulo \(m\) has period dividing \(2m\), and
\[T(2m-1-n)\equiv T(n)\pmod m.\]
The involution \(n\mapsto2m-1-n\) has no fixed indices and exchanges the first \(m\) indices with the last \(m\). Thus the number of solutions in the first \(m\) indices is half the number among the first \(2m\). For \(m=2^a q\), with \(q\) odd, CRT applied to inputs modulo \(2^{a+1}q=2m\) and to congruences modulo \(2^a\) and \(q\) gives exactly twice the number of square roots of \(1+8t\) modulo \(q\). The half-period involution cancels this factor of two. This proves the theorem, including the striking identity \(M_{2^a q}(t)=M_q(t\bmod q)\) for every \(a\ge0\) when \(q\) is odd.

**4. Image size and squarefree spectrum.** For \(p^e\), square residues comprise zero and all residues of even valuation \(2j<e\) with a unit quadratic residue; their number is \(1+\sum_{j=0}^{\lfloor(e-1)/2\rfloor}\varphi(p^{e-2j})/2=C_{p,e}\). Counting independently by CRT proves the image and saturation formulas. If \(q\) is a product of \(r\) distinct odd primes, the local positive fiber sizes are one for a zero discriminant and two for a nonzero square discriminant. Both occur at every odd prime, so all powers \(2^0,\ldots,2^r\) occur. The factor \(2\) supplies no additional multiplicity level, by Step 3. This gives the stated sharp parity boundary.

## Verification
The accompanying `verify_triangular.py` independently enumerates every residue and first-block multiplicity for all \(1\le m\le750\), checking the exact formula without using the source recurrence. It separately verifies the odd prime-power root counts and the uniform doubling lift through a range of composite odd parts. Successful run: `VERIFY_OK moduli=750 all_fibers=exact primepowers=checked doubling_lift=checked`. These are finite crosschecks, not the proof for infinitely many moduli.

## Relationship to prior work
Ulness, *Structure of Triangular Numbers Modulo m* (2022), develops triangular-residue occupancy, multiplicity and saturation and explicitly leaves as Conjectures 1 and 2 the prime-power saturation pattern and invariance on multiplication by powers of two. Its Conjecture 3 predicts a multiplicity spectrum for squarefree products of primes. The exact first-block fiber formula settles the two saturation predictions and specifies the necessary parity correction to the third. The source's quadratic-discriminant characterization and reflection identity are used with attribution; the additional local root enumeration and all-modulus first-block fiber product are made explicit here. An independent proof of quadratic-residue counts is included as the local root argument, rather than treating the published conjectures themselves as evidence.

The On-Line Encyclopedia of Integer Sequences, A279085, gives a previously recorded *empirical* closed form for the number of distinct endings modulo powers of ten. That numerical family is a special case of the image formula and is not independently claimed as a new sequence.

## Limitations
The result describes triangular numbers and their first-block residue multiplicities only; it does not describe ordering or gaps between successive occurrences. A general result phrased directly for quadratic congruence fibers could imply parts of the formula even without using triangular-number terminology. The checked literature contains no explicit complete first-block classification, but bibliographic priority outside the inspected sources is not certified. Independent external mathematical audit has not been performed.

## References
1. D. J. Ulness, “Structure of Triangular Numbers Modulo m,” *AppliedMath* **2** (2022), 326–358. DOI: 10.3390/appliedmath2030020; published 1 July 2022. Relevant material: Sections 2–6, including Theorems 1, 5, 8, 17–18 and Conjectures 1–3.
2. OEIS Foundation, A279085, “Number of distinct residues of triangular numbers mod \(10^n\),” first recorded January 2017; numerical/empirical comparison only.
3. Standard quadratic-congruence facts: Hensel lifting for units at odd primes, valuation classification of square roots, and Chinese remainder theorem, with proofs/reductions supplied above.