# Fourfold covering by majority quadratic residues and the two exceptional prime fields

## Finding
For every prime \(p\ge13\), set \(Q_p=\{x^2:x\in\mathbb F_p^\times\}\). Every \(A\subseteq Q_p\) with \(|A|>|Q_p|/2\) satisfies
\[
4A=\mathbb F_p.
\]
For \(p=11\), every such set satisfies \(5A=\mathbb F_{11}\), but the example \(A=\{1,3,5\}\) has \(4A\ne\mathbb F_{11}\). For \(p=7\), every such set satisfies \(6A=\mathbb F_7\), but \(A=\{1,2\}\) has \(5A\ne\mathbb F_7\). The fourfold guarantee is optimal uniformly over primes at least thirteen: \(A=\{1,3,4,10\}\subseteq Q_{13}\) is a strict-majority set for which \(3A=\mathbb F_{13}\setminus\{0\}\).

## Assumptions and scope
All primes are rational primes. The set \(Q_p\) consists of **nonzero** quadratic residues, of size \((p-1)/2\), and \(hA\) denotes sums of exactly \(h\) elements of \(A\), allowing repetitions, in the additive group of \(\mathbb F_p\). Strict majority means \(2|A|>|Q_p|\). The fourfold conclusion holds for all such sets, not merely sets of a particular shape. The small-prime sharpness witnesses are subsets of \(Q_p\) and meet the strict-majority condition. No claim of an optimal order at every individual prime larger than thirteen is made.

## Proof
We use Cauchy--Davenport: for nonempty \(S,T\subseteq\mathbb F_p\),
\[
|S+T|\ge\min\{p,|S|+|T|-1\}.
\]
In particular, if \(|2A|\ge(p+1)/2\), then \(|4A|=p\).

**Primes congruent to one modulo four.** Write \(p=4m+1\). Then \(|Q_p|=2m\), and strict majority yields \(|A|\ge m+1\). Cauchy--Davenport gives \(|2A|\ge2m+1=(p+1)/2\), and hence \(4A=\mathbb F_p\).

**Character lemma for primes congruent to three modulo four.** Write \(\chi\) for the quadratic character of \(\mathbb F_p\), extended by \(\chi(0)=0\). For either sign \(\varepsilon\in\{-1,1\}\), define
\[
T_\varepsilon=\#\{x\in\mathbb F_p:\chi(x)=\chi(x+1)=\chi(x+2)=\varepsilon\}.
\]
We claim the *exact* character count
\[
T_\varepsilon=\frac{p-5-2\chi(2)}8\qquad(p\equiv3\pmod4).
\]
To verify it, restrict \(x\) to the \(p-3\) elements other than \(0,-1,-2\). For any three signs \(a,b,c\in\{-1,1\}\), the indicator that they are all equal is \((1+ab+ac+bc)/4\). For distinct \(i,j\), the classical identity \(\sum_x\chi((x+i)(x+j))=-1\) follows by an affine substitution from \(\sum_u\chi(u^2-1)=-1\); the latter holds because \(v^2=u^2-1\) has exactly \(p-1\) solution pairs, via \((u-v)(u+v)=1\). After excluding \(0,-1,-2\), the three pair correlations for \((0,1),(0,2),(1,2)\) are respectively \(-1-\chi(2),0,-1-\chi(2)\). Summation gives \((p-5-2\chi(2))/4\) triples with all signs equal. The involution \(x\mapsto-2-x\) reverses their common sign, since \(\chi(-1)=-1\), so precisely half are positive and half negative, proving the displayed formula.

**No critical-length progressions.** Now write \(p=4m+3\ge19\), so \(m\ge4\). Suppose \(Q_p\) contained an arithmetic progression
\[
a,a+d,\ldots,a+md\qquad(d\ne0),
\]
of length \(m+1\). Dividing by \(d\), its \(m+1\) successive elements would all have the same nonzero character \(\chi(d)\), producing at least \(m-1\) triples counted by \(T_{\chi(d)}\). But
\[
m-1-T_{\chi(d)}=\frac{p-9+2\chi(2)}8>0
\]
for \(p\ge19\). This contradiction shows that no such progression exists.

**Four sums in the remaining primes.** Given strict-majority \(A\subseteq Q_p\), if \(|A|\ge m+2\), then \(|2A|\ge2m+3>(p+1)/2\). Otherwise \(|A|=m+1\) and Cauchy--Davenport gives \(|2A|\ge2m+1\). If \(|2A|\ge2m+2=(p+1)/2\), we are done. The sole remaining possibility is
\[
|2A|=2m+1=2|A|-1\le p-2.
\]
By Vosper's critical-pair theorem (applied with the two summands both equal to \(A\)), this forces \(A\) to be an arithmetic progression of length \(m+1\), contrary to the character lemma. Thus always \(|2A|\ge(p+1)/2\), and \(4A=\mathbb F_p\).

**Small fields and sharpness.** At \(p=7\), strict majority means \(|A|\ge2\), and repeated Cauchy--Davenport yields \(|6A|\ge\min\{7,6|A|-5\}=7\); \(A=\{1,2\}\) has \(|5A|=6\). At \(p=11\), strict majority means \(|A|\ge3\), so \(|5A|\ge\min\{11,5|A|-4\}=11\), whereas \(A=\{1,3,5\}\) is a three-term progression with \(|4A|=9\). At \(p=13\), the nonzero residues are \(\{1,3,4,9,10,12\}\); the four-element subset \(\{1,3,4,10\}\) has \(3A=\mathbb F_{13}\setminus\{0\}\) by direct finite enumeration, while the general theorem gives \(4A=\mathbb F_{13}\). This completes the proof.

## Verification
Run `python3 verify_prime_majority.py` using standard Python. It exhaustively checks every strict-majority subset for primes \(7,11,13,17,19,23,29,31\), verifies sharpness witnesses, confirms both character-sign counts for all primes \(7\le p\le127\) congruent to three modulo four, and directly rules out critical-length square-residue progressions for primes \(19\le p\le127\) congruent to three modulo four. It outputs `CERTIFICATE_OK exhaustive_majority_subsets=24275 character_sign_checks=30`. The proof for arbitrary primes uses Cauchy--Davenport, Vosper's theorem, and the proved character identity rather than extrapolating from the finite checks.

## Relationship to prior work
Lacey--Mousavi--Rahimi--Vempati, *Density Bounds in Hua's Theorem for Prime Squares*, arXiv:2610.22747v1, Theorem 1.7, proves a ten-summand majority cover for reduced squares when the modulus is coprime to thirty. It does not imply a four-summand cover even for primes, and excludes the prime seven. Lim, *On the density version of quadratic Waring's problem and the quadratic Waring--Goldbach problem*, arXiv:2508.14939v1, Theorem 1.1, treats at least five summands for sufficiently large prime factors, not the fourfold sharp boundary. The classical theorem of Vosper supplies a necessary inverse statement, but does not identify the quadratic-character obstruction to its exceptional progression case. The present fourfold threshold and exact two exceptional small prime fields are distinct from these statements.

## Limitations
The theorem concerns prime fields, not general prime powers or arbitrary composite moduli. It asserts optimality of the fourfold bound as a **uniform** guarantee through the modulus thirteen, not at every individual prime. The precise behavior at all higher individual primes and other residue-subgroup densities is not determined. The overlap survey may miss an implicit classical consequence or unpublished characterization. No independent external validation is asserted.

## References
1. M. T. Lacey, H. Mousavi, Y. Rahimi, M. N. Vempati, *Density Bounds in Hua's Theorem for Prime Squares*, arXiv:2610.22747v1 (first posted 2026-10-15), especially Theorem 1.7 and Section 4. https://arxiv.org/html/2610.22747v1
2. Z. L. Lim, *On the density version of quadratic Waring's problem and the quadratic Waring--Goldbach problem*, arXiv:2508.14939v1 (first posted 2025-08-20), especially Theorem 1.1 and Section 4. https://arxiv.org/html/2508.14939v1
3. A. G. Vosper, *The Critical Pairs of Subsets of a Group of Prime Order*, Journal of the London Mathematical Society 31 (1956), 200--205, doi:10.1112/jlms/s1-31.2.200; see also the author's addendum, pp. 280--282.
