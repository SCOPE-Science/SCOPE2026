# Dyadic invariance and exact minimum lengths for period-doubling cyclic complexity

## Finding
Let \(p=p_0p_1\cdots=0100010101000100\cdots\) be the binary fixed point of the length-two morphism \(\sigma(0)=01\), \(\sigma(1)=00\). For an integer \(n\ge1\), let \(\mathcal F_n(p)\) be its set of contiguous length-\(n\) factors. Two length-\(n\) words are cyclically conjugate when one is a rotation of the other (without letter complement or reversal). Let \(c_p(n)\) count rotation classes meeting \(\mathcal F_n(p)\).

For **every** integer \(n\ge1\), the map \([u]\mapsto[\sigma(u)]\) is a bijection between rotation classes represented in \(\mathcal F_n(p)\) and those represented in \(\mathcal F_{2n}(p)\). Consequently,
\[
c_p(2n)=c_p(n),\qquad c_p(n)=c_p\bigl(n/2^{\nu_2(n)}\bigr).
\]
The exact locations of the minimum value are
\[
\boxed{c_p(n)=2\quad\Longleftrightarrow\quad n=2^k\text{ for some integer }k\ge0.}
\]
In particular, every odd length at least three has at least three cyclic classes, as does every length with an odd part greater than one.

## Assumptions and scope
Words and factors are finite contiguous binary strings, indexed from zero. The infinite fixed point exists because \(\sigma(0)\) begins with \(0\). The substitution acts by concatenation. Rotation of a word of length \(n\) may use any displacement modulo \(n\); rotation classes may contain words not actually occurring as factors, but are counted only when at least one representative occurs. We use \(\nu_2(n)\) for the greatest exponent of two dividing \(n\). All conclusions concern this particular infinite fixed point and all positive integer lengths, not arbitrary substitutions or shifted infinite words.

Define \(\Delta(0)=0\) and for \(n\ge1\) put
\[
\Delta(n)=\max_{u\in\mathcal F_n(p)} |u|_1-\min_{u\in\mathcal F_n(p)} |u|_1.
\]
Here \(|u|_1\) counts occurrences of the symbol \(1\). The boundedness of these extrema follows from their integer range between zero and \(n\).

## Proof
**1. The substitution gives a surjection on cyclic classes.** Every even-start length-\(2n\) factor of \(p=\sigma(p)\) is \(\sigma(u)\) for some \(u\in\mathcal F_n(p)\). Every odd-start factor, at starting position \(2j+1\), has the form \(b\,\sigma(p_{j+1}\cdots p_{j+n-1})\,0\), where \(b\) is the last symbol of \(\sigma(p_j)\). Rotating its initial \(b\) to the end yields \(\sigma(p_{j+1}\cdots p_{j+n-1}p_j)\), which is a cyclic rotation of \(\sigma(p_j\cdots p_{j+n-1})\). Conversely, every \(\sigma(u)\) with \(u\in\mathcal F_n(p)\) occurs at an even start. Thus every length-\(2n\) cyclic class arises from an image.

**2. The substitution reflects cyclic conjugacy.** For arbitrary binary words \(u,v\) of the same positive length, suppose \(\sigma(u)\) and \(\sigma(v)\) are conjugate. If their conjugating rotation has even displacement, grouping into two-letter blocks recovers a cyclic rotation of \(u\) equal to \(v\), since \(01\) and \(00\) are distinct. If it has odd displacement, the first letter of each image block is always zero, so the rotated image's even positions can all be zero only when **every** odd position of the unrotated image is zero. In that case all its symbols are zero, forcing \(u=v=1^n\). In either case \(u\) and \(v\) are conjugate. Conversely, conjugate source words clearly have conjugate images. Combining this injectivity with step 1 proves the claimed bijection, the equality \(c_p(2n)=c_p(n)\), and its iteration to the odd part of \(n\).

**3. A published abelian-spread recurrence.** Parreau, Rigo, Rowland, and Vandomme [2, Proposition 47], together with the identification of their coded statistic with the abelian complexity of \(p\), give, for every integer \(\ell\ge1\) and \(0\le r<2^\ell\),
\[
\Delta(2^\ell+r)=
\begin{cases}
\Delta(r)+1,&0\le r\le 2^{\ell-1},\\
\Delta(2^{\ell+1}-r),&2^{\ell-1}<r<2^\ell.
\end{cases}
\tag{1}
\]
The referenced recurrence is an established input, not claimed as a new result. Its applicability is direct because the length-\(n\) abelian complexity of a binary word is one plus the range of attainable one-counts: sliding a length-\(n\) window changes the count by at most one, so every integer between the minimum and maximum occurs. The referenced coding sends the counted letters to \(1\)'s of \(p\).

**4. Odd lengths at least three have at least three cyclic classes.** The identity \(p_i\equiv\nu_2(i+1)\pmod2\) follows from the substitution and the recursions \(p_{2i}=0\), \(p_{2i+1}=1-p_i\). It proves aperiodicity: for any proposed positive period \(q\), take \(k>\nu_2(q)\) of parity opposite to \(\nu_2(q)\). Then \(p_{2^k-1}\not=p_{2^k-1+q}\), contradicting period \(q\). Hence \(\Delta(r)\ge1\) for every \(r\ge1\), because \(\Delta(r)=0\) would give identical one-counts to every length-\(r\) factor, and subtracting adjacent window counts would force \(p_{i+r}=p_i\) for all \(i\).

We prove by strong induction that \(\Delta(n)\ge2\) for every odd integer \(n\ge3\). For \(n=3=2^1+1\), equation (1) gives \(\Delta(3)=\Delta(1)+1=2\). For larger odd \(n\), uniquely write \(n=2^\ell+r\) with \(\ell\ge2\) and odd \(1\le r<2^\ell\). If \(r\le2^{\ell-1}\), then (1) and aperiodicity give \(\Delta(n)=\Delta(r)+1\ge2\). Otherwise (1) gives \(\Delta(n)=\Delta(2^{\ell+1}-r)\), whose argument is an odd integer at least five and strictly less than \(n\); apply the induction hypothesis.

Every rotation class has one fixed number of ones, hence \(c_p(n)\) is at least the number of attained one-counts, \(\Delta(n)+1\). Therefore \(c_p(n)\ge3\) for odd \(n\ge3\). Finally \(c_p(1)=2\) since both letters occur. Step 2 transfers these two conclusions to every positive length via its odd part, proving the precise if-and-only-if assertion. \(\square\)

## Verification
Run `python3 verify.py` (standard Python only). The checker independently generates 65,536 symbols both from the substitution and from the valuation formula, and constructs complete factor sets at lengths 1 through 128 using all three legal adjacent source pairs at substitution depth eight. It counts necklace representatives via Booth's rotation algorithm, tests \(c_p(2n)=c_p(n)\) at lengths 1 through 64, tests the minimum characterization at lengths 1 through 128, checks recurrence (1) at lengths 2 through 128, and independently tests the conjugacy-reflection lemma for every pair of binary words of lengths 1 through 7. These **finite** tests corroborate rather than replace the unrestricted proof and cited recurrence.

## Relationship to prior work
Cassaigne, Fici, Sciortino, and Zamboni [1, Section 5.1, Proposition 17] introduced cyclic complexity in this setting and proved that the period-doubling word has cyclic complexity two along powers of two, hence lower limit two. That established result is expressly credited. The result here adds an all-length substitution-bijection law and excludes every non-power-of-two length from the minimum. Parreau, Rigo, Rowland, and Vandomme [2, Proposition 47] supply the abelian-spread recurrence used only for the exclusion; their paper concerns abelian and higher-order abelian complexity, rather than counting rotations. Neither inspected full paper asserts the present complete cyclic minimum-length characterization. Related future or unindexed equivalent formulations could remain undiscovered; search absence is not a proof of novelty.

## Limitations
The theorem specifies the full dyadic scaling symmetry and the exact lengths of the minimum but **does not** give a closed form for \(c_p(n)\) at every odd \(n>1\). The lower bound at these odd lengths relies on the previously published abelian-spread recurrence. No independent external audit has been performed. The theorem does not address arbitrary binary substitutions, generalized Cantor words, reversal-equivalence classes, or rotations that do not preserve word length.

## References
[1] Julien Cassaigne, Gabriele Fici, Marinella Sciortino, and Luca Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843, first posted 2014-02-24, Section 5.1, Proposition 17. https://arxiv.org/abs/1402.5843 ; full text https://arxiv.org/pdf/1402.5843

[2] Aline Parreau, Michel Rigo, Eric Rowland, and Elise Vandomme, *A new approach to the 2-regularity of the ℓ-abelian complexity of 2-automatic sequences*, arXiv:1405.3532, first posted 2014-05-14, Sections 6.1–6.2 and Proposition 47. https://arxiv.org/abs/1405.3532 ; full text https://arxiv.org/pdf/1405.3532
