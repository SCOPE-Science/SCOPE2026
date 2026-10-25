# Antisquare rigidity in the Dyck language

## Finding
Let \(\overline{x}\) denote bitwise complementation of a binary word \(x\). An *antisquare of order* \(k\) is a contiguous factor \(x\overline{x}\) with \(|x|=k\). Call a word *good* when it has no antisquare of order at least two (the one-letter antisquares `01` and `10` are permitted).

**Theorem.** For every integer \(n\ge1\), exactly one Dyck word of semilength \(n\) is good. For \(n=1\) this word is `01`; for each \(n\ge2\) it is
\[
G_n=\mathtt{0}^{n-1}\mathtt{10}\mathtt{1}^{n-1}.
\]
Including the empty word, the semilength counting series is \(1/(1-z)\). The fraction of semilength-\(n\) Dyck words that are good is exactly \(1/C_n\), where \(C_n=\frac1{n+1}\binom{2n}{n}\), and therefore is asymptotic to \(\sqrt{\pi}\,n^{3/2}/4^n\). For \(n\ge2\), the unique good word has nesting height \(n-1\).

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), with `0` the opening parenthesis and `1` the closing parenthesis. A Dyck word has as many zeros as ones and every prefix has at least as many zeros as ones. Factors are contiguous; antisquares are **not** abelian squares, ordinary squares, reverse-complement squares, or scattered subsequences. All integer semilengths \(n\ge0\) are covered. The empty Dyck word is good and is counted separately by the constant term.

## Proof
First, any antisquare \(x\overline{x}\) has a number of maximal constant-letter runs congruent to two or three modulo four. Indeed, if \(x\) has an odd number \(r\) of runs, its final letter differs from the first letter of \(\overline{x}\); the concatenation has \(2r\equiv2\pmod4\) runs. If \(r\) is even, the adjoining runs merge, giving \(2r-1\equiv3\pmod4\) runs.

For \(n\ge2\), \(G_n\) has exactly four runs of lengths \((n-1,1,1,n-1)\). A factor of \(G_n\) therefore has at most four runs. Any antisquare factor could have only two or three runs. A two-run antisquare of order at least two has the form \(\mathtt{0}^k\mathtt{1}^k\) or its complement, with \(k\ge2\); it would require two adjacent runs of length at least two, which \(G_n\) lacks. A three-run antisquare has the form \(\mathtt{0}^i\mathtt{1}^{i+j}\mathtt{0}^j\) or its complement, with \(i,j\ge1\). Its middle run has length at least two, whereas every three-run factor of \(G_n\) has one of the two interior singleton runs as its middle run. Thus \(G_n\) is good. The word `01` is good by length.

For uniqueness, use strong induction on semilength. Every nonempty Dyck word has the unique first-return decomposition \(w=\mathtt{0}u\mathtt{1}v\), with Dyck words \(u,v\). Put \(a=|u|/2\), \(b=|v|/2\). If \(w\) is good, then both \(u\) and \(v\), being factors, are good. By induction, each is empty or is the unique word just described at its semilength.

If \(b=0\), then \(w=\mathtt{0}u\mathtt{1}\). The case \(a=0\) gives `01`; \(a=1\) gives `0011`, an antisquare of order two. For \(a\ge2\), the inductive expression yields \(w=G_{a+1}\).

Now suppose \(b\ge1\). If \(a=0\), then \(w=\mathtt{01}v\). For \(b=1\) this is `0101`, namely \(G_2\). For \(b=2\) it is `010101`, an antisquare of order three. For \(b\ge3\), the entire word \(\mathtt{01}G_b\) equals \(x\overline{x}\) with \(x=\mathtt{01}\mathtt{0}^{b-1}\), so it is forbidden.

If \(a\in\{1,2\}\), the word \(u\) ends in `01`; the junction from \(u\) through the following `1` to the leading `0` of \(v\) contains `0110`, an antisquare of order two. Finally, if \(a\ge3\), then \(\mathtt{0}u\mathtt{1}=\mathtt{0}^{a}\mathtt{10}\mathtt{1}^{a}\). If \(b=1\) or \(b=2\), the word \(v\) begins `01`, and \(w\) begins the antisquare \(x\overline{x}=\mathtt{0}^{a}\mathtt{10}\mathtt{1}^{a}\mathtt{01}\), with \(x=\mathtt{0}^{a}\mathtt{10}\). If \(b\ge3\), then \(v\) begins `00`, so the junction contains `1100`, an antisquare of order two. Every excluded case is impossible, proving uniqueness for all \(n\).

There is exactly one good Dyck word of every positive semilength, so the series is \(1+\sum_{n\ge1}z^n=1/(1-z)\). The number of all Dyck words is \(C_n\); standard Catalan asymptotics \(C_n\sim 4^n/(\sqrt\pi n^{3/2})\) give the stated fraction. The height of \(G_n\) reaches \(n-1\) at the end of its initial zero-run and cannot exceed it later. QED.

## Verification
The standalone standard-library program `verify.py` generates all \(290{,}511\) nonempty Dyck words of semilengths one through twelve, tests **all** antisquare orders at least two by direct substring-complement comparison, and finds precisely the stated survivor at each semilength. It separately checks the explicit survivors through semilength eighty and all \(361\) first-return combinations with component semilengths from zero through eighteen. Run `python3 verify.py` from this package. These finite checks corroborate but do not replace the all-length induction.

## Relationship to prior work
Baranwal–Currie–Mol–Ochem–Rampersad–Shallit, *Antisquares and Critical Exponents*, define good binary words, enumerate minimal forbidden antisquares (Theorem 11), and establish that unrestricted good words grow exponentially (Theorem 19). Their Lemma 15 contains the family of longer antisquare obstructions used in the induction here, but their results do not state the intersection of good words with the Dyck language or this one-per-semilength classification. The present proof reuses elementary antisquare families, not a new classification of all minimal antisquares. Mol–Rampersad–Shallit, *Dyck Words, Pattern Avoidance, and Automatic Sequences*, classify other repetition-avoidance phenomena in Dyck words and give the first-return formalism; that paper does not analyze antisquare avoidance. Here the all-length intersection collapses to one word per semilength although the unrestricted good-word language is exponentially large.

## Limitations
This is a classification of *linear* Dyck words, not circular words, arbitrary balanced words, higher-alphabet Dyck languages, or antisquare avoidance in infinite words. It allows order-one antisquares, which occur necessarily in nontrivial binary Dyck words. No optimality assertion for other notions of pseudorepetition is made. The proof is self-contained; the literature comparison is subject to the possibility of equivalent unindexed or differently named results. No independent mathematical audit has been performed.

## References
1. A. Baranwal, J. Currie, L. Mol, P. Ochem, N. Rampersad, and J. Shallit, *Antisquares and Critical Exponents*, arXiv:2209.09223, first posted 2022-09-19; Discrete Mathematics & Theoretical Computer Science 25:2 (2023), DOI 10.46298/dmtcs.10063. Theorem 11, Lemma 15, Proposition 18, Theorem 19.
2. L. Mol, N. Rampersad, and J. Shallit, *Dyck Words, Pattern Avoidance, and Automatic Sequences*, arXiv:2301.06145, first posted 2023-01-15; Communications in Mathematics 33 (2025), MSC2020 68R15, Sections 1–2.
