# Exact cyclic-rotation richness of the period-doubling word

## Finding

Let \(p\) be the one-sided fixed point beginning with zero of the uniform substitution \(\sigma(0)=01\), \(\sigma(1)=00\). For each integer \(n\ge1\), let \(F_n\) be the set of distinct length-\(n\) contiguous factors of \(p\), and let \(\operatorname{Rot}(w)\) denote all distinct cyclic rotations of a finite word \(w\). Define the *maximum occurring rotation multiplicity* by

\[
M(n)=\max_{w\in F_n}\bigl|F_n\cap\operatorname{Rot}(w)\bigr|.
\]

**Theorem.** Write \(n=2^k m\) uniquely with \(k\ge0\) and positive odd \(m\). Then

\[
\boxed{M(n)=\begin{cases}n,&m=1,\\3\cdot2^k,&m\ge3.\end{cases}}
\]

Consequently, a primitive length-\(n\) factor whose entire set of \(n\) rotations occurs in \(p\) exists if and only if \(n=2^k\) or \(n=3\cdot2^k\), for some \(k\ge0\). More strongly, for every integer \(n\ge2\), substitution induces a bijection of occurring cyclic-rotation classes at lengths \(n\) and \(2n\) that doubles the cardinality of **each** class.

## Assumptions and scope

All positions are indexed from zero; factors and rotation classes count distinct finite words, not occurrence positions. A rotation class at length \(n\) is the intersection \(F_n\cap\operatorname{Rot}(w)\), not the full orbit in the space of all binary words. A *primitive* word is not a proper power of a shorter nonempty word. The theorem covers every positive integer \(n\), not merely substitution lengths.

Write \(R\) for the one-step cyclic left rotation. The defining substitution gives \(p_{2i}=0\) and \(p_{2i+1}=1-p_i\) for every integer \(i\ge0\). In particular, \(p\) has no factor \(11\), since a putative pair of consecutive ones would include an even position. It has no factor \(0000\): any such four-position window contains two consecutive odd-indexed zero entries, which would force consecutive ones in \(p\) by the odd-position identity.

## Proof

**1. Class-size doubling.** For every integer \(n\ge1\), the factor sets satisfy the exact identity

\[
F_{2n}=\{\sigma(u):u\in F_n\}\ \cup\ \{R\sigma(u):u\in F_n\}.
\]

Indeed, an even-starting length-\(2n\) factor is a concatenation of \(n\) substitution blocks; an odd-starting one starts at the second symbol of a block and finishes with the first symbol of the following block, which is zero. This is precisely \(R\sigma(u)\). Conversely each listed factor occurs at a corresponding position of \(p\).

For \(n\ge2\), these two families are disjoint. Every even relative position of \(\sigma(u)\) is zero; every odd relative position of \(R\sigma(v)\) is zero. If the two were equal, all positions would be zero and hence \(u=1^n\), forbidden by the absence of \(11\). Both maps are individually injective. For any two length-\(n\) words \(u,v\), the words \(\sigma(u),\sigma(v)\) are cyclic conjugates if and only if \(u,v\) are: an even rotation corresponds exactly to rotating the substituted blocks, while an odd rotation would equate the disjoint phases and is impossible. Therefore the occurring rotation class corresponding to a class \(C\subseteq F_n\) is exactly

\[
\{\sigma(u),R\sigma(u):u\in C\},
\]

which contains \(2|C|\) distinct members. These sets partition \(F_{2n}\) and provide the claimed bijection for \(n\ge2\). The excluded base case is explicit: \(F_1=\{0,1\}\), while \(F_2=\{00,01,10\}\), whose occurring rotation-class cardinalities are one and two.

**2. Universal upper bound at odd lengths.** Let \(m\ge3\) be odd. In \(p\), all ones occur at odd absolute positions. Hence the distances between successive ones *within* any linear factor are even. Consider a length-\(m\) factor \(w\) having at least one one. Among the circular distances between successive ones in \(w\), exactly one is odd: the closing distance from the last one back to the first. This holds also when there is only one one, in which case that distance is \(m\). Denote the unique odd circular gap by \(g\).

Whenever a cyclic rotation of \(w\) is itself a factor of \(p\), its unique odd circular gap must cross the linear boundary. Let \(s\) and \(t\) be the counts of zeros at the beginning and end of this linear factor. Then \(s+t=g-1\). Since \(p\) has no four consecutive zeros, \(0\le s,t\le3\). Therefore odd \(g\) is one of \(1,3,5,7\), and the number of possible positions at which the cyclic word may be cut inside this gap is at most, respectively, \(1,3,3,1\). Thus every occurring rotation class at odd length \(m\ge3\) has at most three members. An all-zero factor, if present, gives only one member. Hence \(M(m)\le3\).

**3. A sharp triple at every odd length.** First, for every positive even integer \(d=2e\), there exist two ones in \(p\) at positions separated by \(d\). Since \(p_{2j+1}=1-p_j\), this reduces to finding \(j\ge0\) with \(p_j=p_{j+e}=0\). If \(e\) is even, take \(j=0\). If \(e\) is odd, choose \(q\) large enough that \(j=8q+3-e\ge0\). Then \(j\) is even, hence \(p_j=0\), while

\[
p_{8q+3}=1-p_{4q+1}=p_{2q}=0,
\]

so \(p_{j+e}=0\) as required.

Now fix any odd \(m\ge3\). Exactly one of \((m-1)/2\) and \((m+1)/2\) is positive and even; let this value be \(d\). Choose ones at positions \(i\) and \(i+d\). Every one at position \(i\) creates a run of three zeros beginning at position \(2i\), because \(\sigma(1)=00\) and the next even-indexed symbol is zero. Thus the word \(00\) begins at both positions \(2i\) and \(2i+1\). If \(m=2d+1\), choose the beginnings \(2i\) and \(2(i+d)+1\). If \(m=2d-1\), choose the beginnings \(2i+1\) and \(2(i+d)\). In both cases these two beginnings differ by precisely \(m\).

We have therefore found a factor \(00u00\) of total length \(m+2\), where \(|u|=m-2\). Its three consecutive length-\(m\) factors

\[
00u,\qquad0u0,\qquad u00
\]

are successive cyclic rotations of one another. They are pairwise distinct: equality of consecutive rotations forces the word to be constant; equality of the first and third would give a word of odd length with period two, again constant. But the only constant possibility would be all zeros, yielding a forbidden factor of \(m+2\ge5\) zeros. Thus an occurring class has at least three members, proving \(M(m)=3\) for every odd \(m\ge3\).

**4. All lengths and the primitive full-orbit condition.** The length-one base case gives \(M(1)=1\), and the explicit length-two class decomposition gives \(M(2)=2\). By Step 1, \(M(2n)=2M(n)\) for every \(n\ge2\). Iterating and using Step 3 gives the boxed formula for arbitrary \(n=2^k m\). An occurring class can have \(n\) members only if its representative is primitive; conversely class size \(n\) means every one of the \(n\) rotations of its primitive representative occurs. The formula equals \(n\) exactly for odd part \(m=1\) or \(m=3\). This completes the proof.

## Verification

The standalone script `verify.py` implements an *exhaustive finite factor cover*: at each length \(n\), choose a substitution block length at least \(n\). Every length-\(n\) factor lies inside the concatenation of two consecutive blocks, and the occurring adjacent source-letter pairs are exactly `00`, `01`, and `10`. The script enumerates these covers, computes cyclic-class cardinality profiles via canonical minimal rotations, and checks the theorem for every \(1\le n\le192\). It additionally checks exact class-size doubling at every even length in the range and constructs a triple witness for every odd length at most \(191\). Execute `python3 verify.py`; the terminal output ends with `VERIFY_OK`. These tests corroborate, but do not replace, the all-length argument in the proof.

## Relationship to prior work

Cassaigne, Fici, Sciortino, and Zamboni introduced cyclic complexity and proved, in their period-doubling example (Proposition 10), an aggregate value of two cyclic classes at dyadic lengths. That count does not determine how many distinct rotations of one factor can occur at general lengths, nor which lengths support all rotations of a primitive factor. The present all-length formula and sharp odd-gap analysis address these different questions. Bell and Shallit later introduced *Lie complexity*, counting conjugacy classes whose entire rotation orbits occur. That is a closely related invariant, but their accessible abstract gives general automaticity and boundedness results, not the present explicit period-doubling classification. The complete paper was not accessible for a decisive comparison. See the review document for originality risks.

## Limitations

The result determines the largest size of an occurring rotation class at every length, not the complete class-size distribution at arbitrary odd lengths, nor the number of complete classes. The paper by Bell and Shallit was only available in abstract form during the literature comparison, so an unobserved equivalent special-case result remains possible. No claim of independent verification, formal proof certification, or exhaustive literature coverage is made.

## References

1. J. Cassaigne, G. Fici, M. Sciortino, and L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843 (first publicly available 24 February 2014), especially Section 5.1 and Proposition 10. https://arxiv.org/abs/1402.5843
2. J. P. Bell and J. Shallit, *Lie Complexity of Words*, arXiv:2102.03821 (2021). https://arxiv.org/abs/2102.03821
3. É. Charlier, S. Puzynina, and L. Q. Zamboni, *On a Group Theoretic Generalization of the Morse–Hedlund Theorem*, arXiv:1505.03848 (2015). https://arxiv.org/abs/1505.03848
