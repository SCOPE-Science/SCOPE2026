# Sharp \(2\)-binomial rotation spectra for fixed multiletter content

## Finding

Let \(\Sigma=\{a_1,\ldots,a_k\}\) be a finite alphabet with \(k\ge3\), and prescribe positive integer letter multiplicities \(\mathbf c=(c_1,\ldots,c_k)\). Set \(N=\sum_{a=1}^{k}c_a\), \(d=\gcd(c_1,\ldots,c_k)\), and \(L=N/d\). For any word \(w\) with exactly those multiplicities, let \(C_2(w)\) be the number of distinct \(2\)-binomial equivalence classes represented by its \(N\) indexed cyclic rotations. Two words are \(2\)-binomially equivalent when every scattered subsequence of length at most two has equal multiplicity in both.

**Theorem (complete fixed-content spectrum).** For every choice of \(k\ge3\) and positive \(\mathbf c\),

\[
\{C_2(w):\operatorname{Parikh}(w)=\mathbf c\}
=\{L,L+1,\ldots,N\}.
\]

The lower endpoint occurs exactly for words \(w=v^d\), where \(v\) has Parikh vector \(\mathbf c/d\). The upper endpoint is attained by the grouped word \(a_1^{c_1}\cdots a_k^{c_k}\), and a word attains it if and only if it has no proper nonempty directed circular segment with Parikh vector \(j\mathbf c/d\) for any integer \(1\le j<d\).

More precisely, for two different indexed rotation starts \(0\le i<j<N\), the corresponding words are \(2\)-binomially equivalent exactly when the intervening linear segment \(w[i:j]\) has Parikh vector \((j-i)\mathbf c/N\). Consequently, any collision occurs only at distances that are integer multiples of \(L\). There is an explicit constructive path of adjacent unequal-letter exchanges from a lower-endpoint word to an upper-endpoint word along which \(C_2\) changes by at most one per exchange; it visits every possible integer in the stated interval.

## Assumptions and scope

All letters in \(\Sigma\) occur at least once; the alphabet has at least three distinct letters. All rotations are length-\(N\) linear words produced by choosing one of the \(N\) indexed circular starting positions. Repeated identical rotations contribute only one equivalence class. The circular segments in the extremal characterization have lengths strictly between zero and \(N\), and use a single traversal (no multiple laps). The claim concerns *scattered-subsequence* multiplicities, not ordinary contiguous factor counts or the averaged Parikh matrix of a circular word.

## Proof

For a linear word \(u\) and letters \(a,b\), write \(B_{a,b}(u)\) for the number of index pairs \(s<t\) with \(u_s=a\) and \(u_t=b\). Together with the letter counts, these statistics give all subsequence counts of length at most two. The diagonal cases are determined by \(B_{a,a}(u)=\binom{c_a}{2}\), independent of rotation.

**1. Exact collision criterion.** Consider two rotation starts \(i<j\), and write the earlier rotation as \(uv\), where \(u=w[i:j]\) is the directed segment of length \(\ell=j-i\). The later rotation is \(vu\). Write \(s_a=|u|_a\) and \(c_a=|uv|_a\). The only pairs whose order changes when \(uv\) becomes \(vu\) are those with one index in each part. For every pair of *distinct* letters \(a,b\),

\[
B_{a,b}(vu)-B_{a,b}(uv)
=(c_a-s_a)s_b-s_a(c_b-s_b)
=c_a s_b-c_b s_a.
\]

All these differences vanish precisely when \(s_a/c_a\) is constant across all \(a\), since every \(c_a>0\). As \(\sum s_a=\ell\) and \(\sum c_a=N\), this constant equals \(\ell/N\). Thus the rotations are equivalent if and only if \(\operatorname{Parikh}(u)=\ell\mathbf c/N\). Writing \(\mathbf p=\mathbf c/d\), the vector \(\mathbf p\) has coprime coordinates. Integrality of \(\ell\mathbf p/L\) implies \(L\mid\ell\) by Bezout's identity. Hence collisions require \(\ell=jL\) for some \(1\le j<d\), and then the segment vector is \(j\mathbf p\).

**2. Sharp lower endpoint and its equality case.** The starting positions \(0,1,\ldots,L-1\) have pairwise different residues modulo \(L\); by the collision criterion, their rotation profiles are all distinct. Thus \(C_2(w)\ge L\). Taking any word \(v\) with Parikh vector \(\mathbf p\), its \(d\)-fold repetition \(v^d\) has identical literal rotations at indices differing by \(L\), so \(C_2(v^d)\le L\), giving equality.

Conversely, if \(C_2(w)=L\), no two different residues modulo \(L\) can share an equivalence class, so all indexed starts sharing one residue do share one class. Hence every length-\(L\) window starting at an index \(0\le i\le N-L\) has Parikh vector \(\mathbf p\): for \(i<N-L\) use equivalent starts \(i\) and \(i+L\), and for \(i=N-L\) use the complementary segment or equivalence to the start at zero. Subtracting consecutive window vectors yields \(\mathbf e_{w_{i+L}}-\mathbf e_{w_i}=0\) for every \(0\le i<N-L\). Therefore \(w_i=w_{i+L}\) everywhere defined, hence \(w=v^d\) with \(v=w[0:L]\). When \(d=1\), the same assertion is tautological with \(v=w\).

**3. Sharp upper endpoint (the alphabet threshold).** Trivially \(C_2(w)\le N\). Consider the word \(g=a_1^{c_1}a_2^{c_2}\cdots a_k^{c_k}\) as a circular concatenation of \(k\) monochromatic runs. Suppose two distinct rotations of \(g\) were equivalent. By step 1, the intervening proper circular segment would contain exactly \(j c_a/d\) copies of *each* letter \(a\), for some \(1\le j<d\); each such count lies strictly between zero and \(c_a\). Thus the segment would have to meet every one of the \(k\) monochromatic runs partially, containing some but not all of each run. A single proper circular interval has only two endpoints and can meet at most two disjoint monochromatic runs partially. Since \(k\ge3\), this is impossible. Hence \(C_2(g)=N\). Applying the collision criterion directly gives the stated characterization of all maximizers.

**4. No missing intermediate values.** For a fixed word \(w=w_0\cdots w_{N-1}\), let \(\mathbf P_i\) be the vector counting letters in the prefix \(w[0:i]\), and put

\[
\mathbf H_i=N\mathbf P_i-i\mathbf c,\qquad 0\le i<N.
\]

For \(i<j\), equality \(\mathbf H_i=\mathbf H_j\) is equivalent to \(\operatorname{Parikh}(w[i:j])=(j-i)\mathbf c/N\), which by step 1 is equivalent to equality of the corresponding \(2\)-binomial profiles. Therefore \(C_2(w)\) is exactly the number of distinct vectors in \(\{\mathbf H_0,\ldots,\mathbf H_{N-1}\}\).

Now exchange two adjacent positions \(t,t+1\) in a linear representation of \(w\), where \(0\le t<N-1\). Every prefix Parikh vector except \(\mathbf P_{t+1}\) is unchanged, so every \(\mathbf H_i\) except \(\mathbf H_{t+1}\) is unchanged. Replacing one member of a finite multiset changes its number of distinct values by at most one. Thus any adjacent exchange changes \(C_2\) by at most one. All words with fixed content are connected by adjacent exchanges: bubble-sort the letters of a lower-endpoint word \(v^d\) into the grouped word \(g\). Along this finite path, \(C_2\) begins at \(L\), ends at \(N\), remains integer-valued, and changes by at most one at each step. It therefore assumes every integer between \(L\) and \(N\). This completes the proof.

## Verification

The standalone program `checker.py` implements two independent ways to count the rotation classes: direct scattered-subsequence pair counts for every rotation, and the centered prefix-vector criterion \(\mathbf H_i\). It exhaustively checks all labeled words with fixed content in the eight cases

\[
(2,2,2),\ (3,3,3),\ (2,2,4),\ (2,4,6),\ (2,2,2,2),\ (2,2,1),\ (1,1,1),\ (1,2,3).
\]

These comprise 18,666 words, and the two methods agree for every one. The checker independently tests the lower equality characterization, the upper balanced-segment criterion, and the full interval of attainable values. For each prescribed content it also constructs an adjacent-swap path and checks that successive class counts differ by at most one. For example, the number of **labeled words** with content \((2,2,2)\) realizing class counts \(3,4,5,6\) is respectively \(6,18,54,12\); for content \((3,3,3)\), counts \(3,4,5,6,7,8,9\) occur with frequencies \(6,54,270,486,576,216,72\). These finite tests are corroborative; the proof covers every length and every positive multiletter composition.

Reproduce with `python3 checker.py`, using only the Python standard library.

## Relationship to prior work

Rigo and Salimov introduced and studied \(m\)-binomial equivalence and its factor-complexity function; the publicly available 2013 conference preprint was posted by May 27, 2013, and their extended 2015 manuscript discusses binary cyclic shifts in its proof of rational frequencies (Theorem 16). Rao, Rigo, and Salimov (2013) study avoidance of \(2\)-binomial powers, not fixed-content spectra of rotation classes. Poovanandran, Simpson, and Teh (2021) treat subword counts in circular words via averaging over conjugates and study ambiguity between *circular words*; averaging is not the same invariant as counting distinct \(2\)-binomial signatures among the conjugates of one word.

The behavior of words with only two occurring letters differs: for example, with content \((2,2)\), the four indexed rotations can represent at most three \(2\)-binomial profiles. In contrast, the grouped three-letter word with content \((2,2,2)\) has six distinct rotation profiles. The result here establishes the full all-content spectrum specifically for three or more positive-content letters. Its proof uses the multiletter lattice walk and the circular partial-run obstruction; it does not claim novelty for the underlying definition of binomial equivalence. The accessible literature comparisons did not identify a previously published theorem implying this exact all-compositions, all-values multiletter spectrum; that absence is not a proof of historical priority.

## Limitations

The theorem only concerns equivalence by subsequences of length at most two, not higher \(m\)-binomial equivalence. It assumes at least three *occurring* letters; an alphabet with unused symbols must be reduced to its support. The statement is about rotations of a single finite word, not the binomial complexity of all factors in an infinite word. It does not count how many words realize each possible value beyond the finite examples shown. No independent mathematical audit or exhaustive historical-priority certification has been performed.

## References

1. M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, WORDS 2013, LNCS 8079, 217–228. Author preprint publicly available 2013-05-27 at https://orbi.uliege.be/handle/2268/149313 . Extended version: *Theoretical Computer Science* 601 (2015), 47–57, https://orbi.uliege.be/bitstream/2268/178703/1/binomial_TCS_final.pdf .
2. M. Rao, M. Rigo, and P. Salimov, *Avoiding 2-binomial squares and cubes*, arXiv:1310.4743, first submitted 2013-10-17, https://arxiv.org/abs/1310.4743 .
3. G. Poovanandran, J. Simpson, and W. C. Teh, *Counting Subwords in Circular Words and Their Parikh Matrices*, arXiv:2110.14858, first submitted 2021-10-28, https://arxiv.org/abs/2110.14858 .
