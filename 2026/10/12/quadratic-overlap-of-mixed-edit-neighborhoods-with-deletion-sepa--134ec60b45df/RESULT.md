# Quadratic overlap of mixed-edit neighborhoods with deletion-separated centers

## Finding
For every integer \(n\ge4\), two distinct binary length-\(n\) words \(x_n,z_n\) exist such that
\[
D_1(x_n)\cap D_1(z_n)=\varnothing,
\qquad
\bigl|I_1(D_1(x_n))\cap I_1(D_1(z_n))\bigr|=\left\lfloor\frac{n^2}{4}\right\rfloor+4.
\]
Here \(D_1\) deletes exactly one symbol and \(I_1\) inserts exactly one symbol, with duplicate outputs counted once. Consequently, in a two-codeword single-deletion-correcting code, at least \(\lfloor n^2/4\rfloor+5\) **distinct** outputs from the composed channel are needed to guarantee reconstruction in the worst case. This is an existence lower bound, not a universal upper bound or a claim of maximization over all pairs.

## Assumptions and scope
The alphabet is \(\{0,1\}\), the blocklength is any integer \(n\ge4\), and both channel operations occur in the order one deletion, then one insertion. For a word \(u\), \(D_1(u)\) is a set of words of length one less; \(I_1(S)=\bigcup_{s\in S}I_1(s)\). Juxtaposition means concatenation, and \((01)^r\) denotes \(r\) repetitions of the displayed two-bit block. Write \(n=4r+c\) with \(r\ge0\) and \(c\in\{4,5,6,7\}\); these four representations partition all \(n\ge4\). Define \(x_n=u_c\,0110\,v_c\) and \(z_n=u_c\,1001\,v_c\), with
\[
\begin{array}{c|cc}
c&u_c&v_c\ \hline
4&(01)^r&(01)^r\
5&(01)^r0&(10)^r\
6&(01)^r0&1(01)^r\
7&(01)^{r+1}&0(10)^r
\end{array}.
\]
The subscript \(c\) in \(u_c,v_c\) suppresses the parameter \(r\).

## Proof
**Deletion separation.** The two strings disagree exactly in the four consecutive central positions. If two equal-length strings share a length-one-shorter subsequence, one is transformed to the other by moving a single symbol. Consequently, outside some interval they coincide, and within that interval one word is the other shifted by one position. The interval must include the four positions where these two strings differ. In a forward shift, every internal position of that interval must differ from its successor; in a backward shift, it must differ from its predecessor. Both are impossible because the two middle symbols of 0110 are equal (11). Thus \(D_1(x_n)\cap D_1(z_n)=\varnothing\). Both central blocks have a common two-symbol subsequence, so the fixed-length Levenshtein distance between the centers is exactly two, although this last observation is not needed for the bound.

**Exact neighborhood intersection by a finite automaton.** Membership of a target word \(w\) in \(I_1(D_1(x))\) is equivalent to transforming \(x\) to \(w\) by either zero changes, one substitution, or one contiguous shift by one position (with arbitrary inserted bit and arbitrary deleted bit). A six-state nondeterministic scanner recognizes these three possibilities when reading aligned symbol pairs \((x_i,w_i)\). Its state bits encode: pre-operation; post-operation; forward-shift pending bit zero or one; and backward-shift pending bit zero or one. The exact transition is given in the complete standalone source `verify_mixed.cpp` and independently reproduced in `verify_direct.py`. All nonempty end states are accepting, including a shift pending at the last position. Determinizing the product of two such scanners for \(x\) and \(z\), with shared output \(w\), gives exactly 64 reachable composite states. This recognizer is deterministic in \(w\); hence its accepting-path count equals the **number of distinct common outputs**, not the number of edit scripts.

Let \(T_{ab}\), for \(a,b\in\{0,1\}\), be the 64-square integer transition matrix for fixed input pair \((a,b)\), summing the two possible output bits. Set
\[
P=T_{00}T_{11},\qquad Q=T_{11}T_{00},\qquad
C=T_{01}T_{10}T_{10}T_{01}.
\]
For \(c=4,5,6,7\), define \((K_c,R_c)\) respectively by
\[
(C,P),\quad(T_{00}C,Q),\quad(T_{00}CT_{11},P),\quad(PC T_{00},Q).
\]
Let \(e\) be the initial-state coordinate column and \({\bf1}\) the all-ones column. The exact intersection size for \(n=4r+c\) is
\[
a_c(r)=e^{\mathsf T}P^rK_cR_c^r{\bf1}.
\]
This follows directly from the four explicitly defined concatenation patterns; the center contributes \(C\). As \(X_{r+1}=PX_rR_c\) with \(X_0=K_c\), the vectorized matrix sequence evolves by a single linear operator on a 4096-dimensional rational vector space. Cayley–Hamilton implies that each scalar \(a_c(r)\) obeys a monic linear recurrence of order at most 4096. The proposed value \(b_c(r)=\lfloor(4r+c)^2/4\rfloor+4\) is a quadratic polynomial in integer \(r\) (for fixed \(c\)), hence its third forward difference vanishes. Therefore \(a_c(r)-b_c(r)\) satisfies a monic recurrence of order at most 4099. Equality for the first 4099 consecutive values \(r=0,\ldots,4098\) forces equality for all \(r\ge0\).

The supplied C++17 verifier constructs all 64 reachable states and the four exact matrices from the scanner transitions, and checks these **4099 initial values for each of the four residues** using unsigned 64-bit integer arithmetic. There is no floating-point or randomized step. Overflow cannot occur: starting from any scanner-state subset, accepted outputs over a fixed length are a union of at most six languages, each generated by at most a quadratic number of locations and two inserted-bit choices. A conservative bound of \(12(L+1)^2\) holds for each such language count of length \(L\); at the largest verified length (below 16400), this is less than \(2^{32}\). The matrix products count distinct deterministic output paths, so intermediate nonnegative sums are bounded by the same fixed-length language count, below \(2^{64}\). The verification of the finite base, together with the recurrence theorem, is an **infinite proof**, not an extrapolation from samples.

## Verification
Compile and run `c++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_mixed.cpp -o verify_mixed && ./verify_mixed`. The expected final line is `VERIFY_OK states=64 matrix_dimension=4096 initial_terms_per_residue=4099 all_n_at_least_4=proved`. Run `python3 verify_direct.py` to independently construct deletion/insertion output sets, compare them with the scanner for every unordered pair through length eight, and check each displayed family through length fourteen. The expected final line begins `DIRECT_VERIFY_OK all_pairs_n_le_8= 43942`.

## Relationship to prior work
Sala, Gabrys, Schoeny and Dolecek (2016, Section V-B) introduce the composed deletion–insertion ball and exhibit a large intersection for **alternating centers of fixed-length Levenshtein distance one**, in the *uncoded* reconstruction problem. Their construction does not enforce disjoint one-deletion shadows. Here the centers instead have distance two, so they are a two-word single-deletion-correcting code. Cai, Kiah, Nguyen and Yaakobi study reconstruction from *single-edit alternatives* such as one insertion **or** one deletion; that output model differs from their composition to an equal-length output. Bar-Lev, Etzion and Yaakobi determine properties of the **size of one radius-one fixed-length Levenshtein ball**, not this pairwise intersection. Bar-Lev, Sabary, Gershon and Yaakobi study the intersection of **an insertion ball with a deletion ball** about two words of possibly different lengths, not the intersection of two *composed* balls. These comparisons are based on material inspection of the pertinent papers; absence of an identified covering publication is not proof of priority.

## Limitations
No claim is made that the exhibited overlap is the maximum among all pairs at fixed-length Levenshtein distance two, or that the two-word obstruction yields a general optimal coding rate. The proved read bound concerns distinct adversarial outputs; noisy repeated identical outputs do not help. Earlier unindexed specializations of radius-one Levenshtein ball intersections remain possible. This is a computationally assisted exact theorem based on a disclosed finite-state construction and a 4099-term certificate; it has not undergone independent external audit.

## References
1. F. Sala, R. Gabrys, C. Schoeny and L. Dolecek, *Exact Reconstruction from Insertions in Synchronization Codes*, arXiv:1604.03000, first public version 11 April 2016. https://arxiv.org/abs/1604.03000
2. K. Cai, H. M. Kiah, T. T. Nguyen and E. Yaakobi, *Coding for Sequence Reconstruction for Single Edits*, arXiv:2001.01376. https://arxiv.org/abs/2001.01376
3. D. Bar-Lev, T. Etzion and E. Yaakobi, *On Levenshtein Balls with Radius One*, arXiv:2103.01681. https://arxiv.org/abs/2103.01681
4. D. Bar-Lev, O. Sabary, Y. Gershon and E. Yaakobi, *The Intersection of Insertion and Deletion Balls*, IEEE Information Theory Workshop (2021), doi:10.1109/ITW48936.2021.9611515.
