# Prime-order onset and first ambiguous fibers for signed four-atom Fourier phase retrieval

## Finding
Let \(p\ge5\) be prime and let \(\mathcal S_p\) be the set of functions \(f:\mathbb Z_p\to\{-1,0,1\}\) with exactly four nonzero entries. Write
\[
\widehat f(k)=\sum_{x\in\mathbb Z_p} f(x)e^{-2\pi i kx/p},
\qquad I_f(k)=|\widehat f(k)|^2.
\]
Call two signals trivially equivalent if one is obtained from the other by a common sign, a cyclic translation, or a reflection followed by a translation. Then:

1. If \(p=5\) or \(p=7\), equality \(I_f=I_g\) implies trivial equivalence. The respective counts of spectra (and of trivial-equivalence classes) are \(6\) and \(26\).
2. For \(p=11\), there are exactly \(135\) distinct indexed power spectra of signals in \(\mathcal S_{11}\), and exactly \(140\) trivial-equivalence classes. Exactly five spectra have two distinct trivial-equivalence classes each; every other spectrum has one. Those five, and only those five, have inverse-Fourier autocorrelation
\[
C(0)=4,\qquad C(\pm d)=-1,\qquad C(\pm2d)=1,
\qquad C(t)=0\text{ otherwise},
\]
with \(d\in\{1,2,3,4,5\}\). The signs and residues in the displayed prescription are taken in \(\mathbb Z_{11}\).
3. Every prime \(p\ge11\) admits an inequivalent pair of signals in \(\mathcal S_p\) with identical power spectra. Hence \(11\) is the least prime order supporting a nontrivial signed four-atom ambiguity.

An explicit pair, valid for every \(p\ge11\), has generating polynomials
\[
F(z)=-1-z-z^7+z^8,
\qquad H(z)=-1+z^2+z^4+z^8.
\]
The polynomials have equal modulus on the entire complex unit circle, not merely on the sampled \(p\)-th roots of unity.

## Assumptions and scope
The Fourier transform above is unnormalized and its intensities are **indexed** by \(k\in\mathbb Z_p\); an arbitrary permutation of frequencies is not an allowed ambiguity. The signal alphabet and exact support cardinality are fixed. The only equivalences quotiented out are translations, reflections, and multiplication by the common sign \(\pm1\). The complete fiber count is asserted only for \(p=5,7,11\); for larger primes only existence of an inequivalent pair is claimed. No classification of general complex-amplitude signals is asserted.

## Proof
**1. Autocorrelation criterion.** Define \(C_f(t)=\sum_x f(x)f(x-t)\). Expanding the Fourier intensity yields
\[
I_f(k)=\sum_{t\in\mathbb Z_p} C_f(t)e^{-2\pi i kt/p}.
\]
Fourier inversion therefore shows that \(I_f=I_g\) exactly when \(C_f=C_g\). Translation, reflection, and global sign preserve this real symmetric autocorrelation.

**2. Exhaustive, exact small-prime certificate.** Every \(f\in\mathcal S_p\) is trivially equivalent to a signal that has \(f(0)=1\): translate one of its four nonzero positions to zero, then apply a global sign. The other three positions are an unordered triple of distinct elements of \(\{1,\dots,p-1\}\); each of their signs has two choices. Thus the following pseudocode enumerates all relevant signals, with no missing orbit:

```python
for S in combinations(range(1,p), 3):
    for signs in product((1,-1), repeat=3):
        pts = ((0,1),) + tuple(zip(S,signs))
        intensity_key = tuple(sum(a*b for x,a in pts for y,b in pts
                                  if (x-y) % p == t) for t in range(p))
        fibers[intensity_key].add(canonical_dihedral_signed_orbit(pts,p))
```

The canonical orbit representative is the lexicographic minimum of the sorted lists of the four \((\text{position},\text{sign})\) pairs after applying every reflection direction, both global signs, and every translation that places one of the four support points at zero. This searches a complete set of transformations: any shift, reflection, and sign can be followed by an anchoring shift; the resulting representative set contains precisely one canonical key per orbit. The accompanying executable `checker.py` implements the pseudocode using integer arithmetic only.

The exhaustive results are:

| Prime order | Anchored configurations | Distinct autocorrelations | Trivial-equivalence classes | Spectra with two classes |
|---|---:|---:|---:|---:|
| \(5\) | \(32\) | \(6\) | \(6\) | \(0\) |
| \(7\) | \(160\) | \(26\) | \(26\) | \(0\) |
| \(11\) | \(960\) | \(135\) | \(140\) | \(5\) |

For \(p=11\), every fiber has size one or two after quotienting, and the five two-element fibers have exactly the displayed autocorrelation profiles. To cross-check completeness at order \(11\), the executable also enumerates **all** \(\binom{11}{4}2^4=5280\) signed four-atom signals, without fixing an anchor, and confirms that they produce the same \(140\) canonical orbits as the anchored enumeration. The finite tables are exact exhaustions of explicitly bounded finite domains, not samples or extrapolations.

**3. A uniform ambiguity and its nontriviality.** The factorizations
\[
\begin{aligned}
F(z)&=(z^2+1)(z^3-z^2+1)(z^3-z-1),\\
H(z)&=(z^2+1)(z^3-z^2+1)(z^3+z^2-1)
\end{aligned}
\]
are exact polynomial identities. The final factor in \(H\) is the negative reversed polynomial of the final factor in \(F\):
\[
z^3+z^2-1=-z^3\bigl(z^{-3}-z^{-1}-1\bigr).
\]
For \(|z|=1\), reversal changes neither modulus nor the other two factors. Thus \(|F(z)|=|H(z)|\), proving the spectral equality for every prime \(p\ge11\), where the four exponent positions in each polynomial remain distinct modulo \(p\).

The coefficient signs of \(F\) consist of one positive and three negative values, while those of \(H\) consist of three positive and one negative value. A hypothetical trivial equivalence must therefore include global sign reversal. After reversing the sign of \(F\), its unique negative position is at \(8\); that of \(H\) is at \(0\). Aligning those unique negative positions forces its three positive positions to be either \(\{-8,-7,-1\}\) or \(\{8,7,1\}\) modulo \(p\). The three positive positions of \(H\) are \(\{2,4,8\}\). Neither coincidence is possible for prime \(p\ge11\): in the first possibility, the set contains \(p-1\), which is never one of \(2,4,8\); in the second, it contains \(1\). Hence these signals are inequivalent. Combining with part 2 proves the sharp onset.

## Verification
Run `python3 checker.py` from the same directory as this document using Python 3.8 or newer. The checker requires only the Python standard library. It computes all periodic autocorrelation entries exactly and performs the full anchored enumeration at orders \(5,7,11\), an unanchored order-\(11\) orbit cross-check, the five-profile comparison, and an integer Laurent-autocorrelation identity for the explicit pair. Its unit-circle equality proof is algebraic as given above, independent of finite testing. The checker also checks the explicit pair in several finite prime orders, as supplementary tests.

## Relationship to prior work
Bendory, Edidin, and Gonzalez study finite-alphabet phase retrieval and the combinatorics of homometric partitions. Their main equivalence in Theorem 4.3 assumes *generic* nonzero alphabet values. Here the prescribed nonzero letters \(\{-1,+1\}\) are fixed and nongeneric; that theorem supplies the motivating Fourier-autocorrelation framework but does not classify these fibers or their prime threshold. Gordon studies signed difference sets with **constant** nonzero-lag autocorrelation; the ambiguous signals here have two different nonzero-lag values and many vanishing lags, so that uniform condition does not subsume the result. Erickson and Jones discuss the known classification of **unsigned** four-point homometric supports; their cited families occur at cyclic orders divisible by \(4\) or \(13\), not at the signed order-\(11\) ambiguity found here. Ordinary polynomial zero flipping explains the all-order witness but not, by itself, the sharp finite-prime threshold or complete order-\(11\) fibers.

## Limitations
The low-order fiber counts use finite exhaustive integer calculations, with the executable provided for complete reproduction. The infinite-prime claim establishes existence of an ambiguity, not a classification of all ambiguous spectra beyond order \(11\). Originality remains subject to earlier signed-sequence catalogs, generalized homometry tables, and spectral-factorization classifications that may encode the same result under different terminology. No independent audit has been carried out.

## References
1. T. Bendory, D. Edidin, and I. Gonzalez, *Finite Alphabet Phase Retrieval*, arXiv:2301.10647 (initial public version January 25, 2023), Theorem 4.3 and Sections 2--6. https://arxiv.org/html/2301.10647v2
2. D. M. Gordon, *Signed Difference Sets*, arXiv:2212.10630, Section 1 and signed-difference-set definition. https://arxiv.org/html/2212.10630v1
3. W. Q. Erickson and N. B. Jones, *Classifying Z-related sets of order 5*, arXiv:2412.08997, Section 1 (summary of the unsigned four-point classification). https://arxiv.org/html/2412.08997v1
