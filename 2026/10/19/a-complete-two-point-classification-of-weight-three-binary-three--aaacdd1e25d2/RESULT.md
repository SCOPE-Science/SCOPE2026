# A complete two-point classification of weight-three binary three-deck fibers

## Finding

For a finite binary word \(w\), its **three-deck** is the vector of eight counts \([w]_u\), one for each \(u\in\{0,1\}^{3}\), where \([w]_u\) counts triples of strictly increasing positions spelling \(u\). For \(n\ge 3\), let \(D_{3,3}(n)\) denote the number of distinct three-decks among length-\(n\) words with exactly three ones, and put \(D_{3,3}(0)=D_{3,3}(1)=D_{3,3}(2)=0\).

**Theorem.** Every three-deck equivalence class in this domain contains either one or two words. The two-word classes, without repetitions, consist precisely of
\[
\begin{split}
 w&=0^{a}\,1\,0^{c+3t}\,1\,0^{c}\,1\,0^{d+t},\\
 w'&=0^{a+t}\,1\,0^{c}\,1\,0^{c+3t}\,1\,0^{d},
\end{split}
\qquad a,c,d\in\mathbb Z_{\ge0},\quad t\in\mathbb Z_{\ge1}.
\]
In particular, the generating function is
\[
\boxed{\sum_{n\ge0}D_{3,3}(n)z^n
=\frac{z^3}{(1-z)^4}-\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)}.}
\]
This proves the exact generating-function identity posed as Conjecture 1 in Chrisnata, Kiah, Karingula, Vardy, Yaakobi, and Yao, *On the number of distinct \(k\)-decks: Enumeration and bounds*, Section 5.3 (2021 online release; 2023 journal issue).

For a uniformly selected length-\(n\) binary word of weight three, the fraction that share their three-deck with another word tends to \(1/4\). Moreover,
\[
D_{3,3}(n)=\frac{7}{48}n^3+O(n^2).
\]
The first ambiguous length is \(n=7\), witnessed by \(1000110\) and \(0110001\).

## Assumptions and scope

The alphabet is the labeled set \(\{0,1\}\), words are linear rather than cyclic, positions must be strictly increasing, and subsequence multiplicities count embeddings (not merely distinct subsequence strings). All word lengths in the theorem are nonnegative integers; the enumeration concerns precisely words with three ones. There are \(\binom n3\) such words at length \(n\ge3\), and the deck length is exactly three, not a collection of deletions leaving three symbols or a contiguous-substring profile.

Each word in this domain has a unique gap representation
\[
w(a,b,c,d)=0^a1\,0^b1\,0^c1\,0^d,
\qquad a,b,c,d\in\mathbb Z_{\ge0},\quad a+b+c+d=N=n-3.
\]

## Proof

**1. Three deck coordinates suffice.** For \(i\in\{1,2,3\}\), let \(p_i\) be the number of zeros before the \(i\)-th one, so that
\[
(p_1,p_2,p_3)=(a,a+b,a+b+c).
\]
Writing \(A=[w]_{011}\), \(B=[w]_{101}\), and \(C=[w]_{001}\), counting embeddings directly gives
\[
\begin{aligned}
A&=3a+b, &B&=2(b+c), &[w]_{110}&=c+3d,\\
C&=\sum_{i=1}^{3}\binom{p_i}{2},
&[w]_{010}&=\sum_{i=1}^{3}p_i(N-p_i),
&[w]_{100}&=\sum_{i=1}^{3}\binom{N-p_i}{2},\\
[w]_{000}&=\binom N3, &&[w]_{111}=1.
\end{aligned}
\]
For \(N=0,1,2\), the usual convention \(\binom Nk=0\) when \(N<k\) applies. The number of zeros before the three ones, summed over those ones, is
\[
S=\sum_{i=1}^{3}p_i=3a+2b+c=A+B/2.
\]
Also \(\sum_i p_i^2=2C+S\). Consequently
\[
[w]_{010}=(N-1)S-2C,
\qquad [w]_{100}=3\binom N2-C-[w]_{010},
\qquad [w]_{110}=3N-A-B.
\]
Thus two weight-three words of equal length have equal complete three-decks **if and only if** their three integers \(A,B,C\) agree. This equivalence is exact, including the zero-length gap and short-length boundaries.

**2. All candidate collisions lie on one integer line.** Suppose gap vectors \(g=(a,b,c,d)\) and \(g'=(a',b',c',d')\) have equal \(N,A,B\). Let \(t=a'-a\). Equality of \(A=3a+b\), equality of \(B=2(b+c)\), and the total-sum constraint successively force
\[
g'=(a+t,b-3t,c+3t,d-t),\qquad t\in\mathbb Z.
\]
Correspondingly, the three zero-prefix counts change by
\[
(p'_1,p'_2,p'_3)=(p_1+t,p_2-2t,p_3+t).
\]
Substitution into the exact formula for \(C\) and expansion of the three binomial coefficients yields
\[
C(g')-C(g)=t(c-b+3t).
\]
If \(g'\ne g\), then \(t\ne0\), and equality of the complete decks forces
\[
b-c=3t.
\]
Therefore \(b'=c\), \(c'=b\) and the only possible other point in the same deck fiber has gap vector
\[
(a+t,c,b,d-t),\qquad t=(b-c)/3\ne0.
\]
For any starting vector \(g\), at most one nonzero integer \(t\) solves this equation. Hence every fiber has size at most two. Conversely, if the displayed partner has nonnegative coordinates, these equations yield equality of \(A,B,C\), which by Step 1 implies equality of the entire deck.

**3. Parametrization is exhaustive and does not double count.** Orient a distinct pair so that \(t>0\). Then \(b=c+3t\), \(d\ge t\), while \(a,c\ge0\). Write \(d=d_0+t\) and rename \(a=a_0\), \(c=c_0\). The two words are exactly the theorem's displayed pair. Every parameter tuple with \(a_0,c_0,d_0\ge0\) and \(t\ge1\) supplies a pair of nonnegative gap vectors with the same deck. The first member always has middle-gap difference \(b-c=3t>0\), while the second has difference \(-3t<0\); this orientation and unique gap representation show that distinct parameter tuples produce distinct two-word fibers.

**4. Enumerate the fibers.** With \(N=n-3\) zeros, the two-word pair associated with \((a_0,c_0,d_0,t)\) has
\[
N=a_0+d_0+2c_0+4t.
\]
Let \(H_N\) count two-word fibers. Its ordinary generating function is therefore
\[
\sum_{N\ge0}H_Nz^N
=\sum_{a_0,d_0,c_0\ge0}\sum_{t\ge1}
 z^{a_0+d_0+2c_0+4t}
=\frac{z^4}{(1-z)^2(1-z^2)(1-z^4)}.
\]
Every fiber is a singleton or a doubleton, so the number of distinct three-decks equals the number of source words minus the number of doubleton fibers:
\[
D_{3,3}(n)=\binom n3-H_{n-3} \quad(n\ge3).
\]
Using \(\sum_{n\ge3}\binom n3z^n=z^3/(1-z)^4\) immediately proves the stated generating function for all lengths. Equivalently, for \(N\ge0\),
\[
H_N=\sum_{t=1}^{\lfloor N/4\rfloor}
\sum_{c_0=0}^{\lfloor(N-4t)/2\rfloor}(N-4t-2c_0+1).
\]
The first possible pair has \(N=4\), proving sharpness of the threshold \(n=7\).

**5. Asymptotics.** At \(z=1\) the pair-count generating function has leading singular part \(1/[8(1-z)^4]\). Other poles are roots of unity of order at most four and contribute only \(O(N^2)\) to coefficients. Hence \(H_N=N^3/48+O(N^2)\), whereas the number of source words is \(\binom{N+3}{3}=N^3/6+O(N^2)\). Thus \(D_{3,3}(n)=7n^3/48+O(n^2)\); since exactly \(2H_N\) source words lie in two-word fibers, the ambiguous-word proportion tends to \(2(1/48)/(1/6)=1/4\).

## Verification

The standalone file `check_decks.py` implements two independent methods of counting each ordered length-three subsequence: a direct combinations-of-positions method for small words and a streaming dynamic program for all cases. It generates every nonnegative gap quadruple of total zero count \(N=0,\ldots,25\), groups by its actual eight-coordinate deck, verifies that every equivalence class is a singleton or exactly the predicted pair, and compares the number of fibers against the independent parameter count. It also probes 500 deterministic larger randomly selected gap vectors and checks admissible candidate companions. Running `python3 check_decks.py` prints `WEIGHT3_3DECK_ALL_CHECKS_PASSED totals=0..25 profiles=23751 random=500` on success. These finite checks corroborate, but do not replace, the all-length proof above.

## Relationship to prior work

Chrisnata et al. defined the exact quantity \(D_{3,3}(n)\), established its cubic order, described the one-dimensional 2-deck nullspace for weight-three words, and stated the displayed generating function as **Conjecture 1** after checking twenty coefficients (journal article Section 5.3, pp. 15–17). The nullspace direction itself, and their lower-bound construction, are established prior results, not new contributions here. What is proved here is the **converse for all collisions**, a two-point classification of every fiber, and a bijective enumeration that establishes their conjecture for every \(n\).

The 2019 conference antecedent discusses general deck bounds but does not provide this all-length formula. Nilforoushan and Parvaresh (2026) give an exact exponent of growth for the number of all binary three-decks across unrestricted weights and an independent-parameter analysis; those results neither enumerate weight-three fibers nor imply this fixed-weight rational generating function. Literature on binomial equivalence of factors of infinite words addresses a different selection problem.

## Limitations

No claim is made for weights other than three, for nonbinary alphabets, for decks of other lengths, or for error-correcting codes under noisy deck observations. The mathematical proof and finite tests do not establish that no independently discovered equivalent proof exists in unindexed or inaccessible literature. No independent external audit or formal proof assistant validation is claimed.

## References

1. J. Chrisnata, H. M. Kiah, S. R. Karingula, A. Vardy, E. Yaakobi, and H. Yao. *On the number of distinct k-decks: Enumeration and bounds*. **Advances in Mathematics of Communications** 17 (2023), 960–978. First available online 2021-08-30. DOI: 10.3934/amc.2021032. Open-access author PDF: https://yaakobi.net.technion.ac.il/files/2022/08/60_k_Decks_Disc_Math21.pdf.
2. J. Chrisnata, H. M. Kiah, S. Rao, A. Vardy, E. Yaakobi, and H. Yao. *On the Number of Distinct k-Decks: Enumeration and Bounds*. ISCIT (2019), pp. 519–524. DOI: 10.1109/ISCIT.2019.8905191.
3. A. Nilforoushan and F. Parvaresh. *Improved upper bound on the number of distinct k-decks for any k and alphabet size by counting the independent parameters*. arXiv:2609.23106 (first posted 2026-09-19), https://arxiv.org/abs/2609.23106.
4. M. Rigo, M. Stipulanti, and M. A. Whiteland. *Characterizations of families of morphisms and words via binomial complexities*. arXiv:2201.04603 (2022), https://arxiv.org/abs/2201.04603.
