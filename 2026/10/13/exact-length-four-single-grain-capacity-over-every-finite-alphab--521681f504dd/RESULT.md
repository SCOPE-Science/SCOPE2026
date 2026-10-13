# Exact length-four single-grain capacity over every finite alphabet

## Finding
For each integer \(q\ge2\), consider words of length four over an alphabet \(Q\) with \(|Q|=q\). A single grain error replaces at most one entry after the first by the symbol immediately preceding it **in the transmitted word**. The largest zero-error code has cardinality
\[
M_q(4,1)=q^3-q^2+q.
\]
This holds for arbitrary alphabets, including non-prime-power cardinalities. An explicit construction uses an idempotent Latin square for \(q\ge3\), and a six-word exception for \(q=2\).

## Assumptions and scope
Index the four positions by \(0,1,2,3\). For a transmitted word \(x=(a,b,c,d)\), define its complete at-most-one-grain output set
\[
B(x)=\{(a,b,c,d),(a,a,c,d),(a,b,b,d),(a,b,c,c)\},
\]
where repeated outputs are identified. A code \(C\subseteq Q^4\) corrects one such error if \(B(x)\cap B(y)=\varnothing\) whenever \(x,y\in C\) are distinct. The first transmitted coordinate is always preserved. No stochastic assumptions or probabilities are involved.

An **idempotent Latin square** on \(Q\) is a map \(L:Q\times Q\to Q\) for which, for each fixed row or column, the other variable runs bijectively over \(Q\), and \(L(z,z)=z\) for every \(z\in Q\). The classical existence theorem for idempotent Latin squares supplies one for every order \(q\ge3\); none exists at order two. For arbitrary \(q\ge3\), fix any such \(L\) and define
\[
C_L=\bigcup_{a\in Q}\left(\{(a,a,a,a)\}\cup
\{(a,b,c,L(b,c)):b\ne a,\ c\in Q\}\right).
\]
Then \(|C_L|=q[1+q(q-1)]\).

## Proof
**Upper bound.** Fix the first symbol \(a\in Q\), and write \(C_a=\{x\in C:x_0=a\}\). Let \(t\) denote the number of words in \(C_a\) whose second symbol is also \(a\). Thus these words have shape \((a,a,c,d)\). Their last coordinates \(d\) must be distinct: a grain at position two transforms all of them into \((a,a,a,d)\). Call their \(t\)-element set of last coordinates \(D\).

Now partition the remaining words of \(C_a\) into (I) \((a,b,a,d)\) with \(b\ne a\), and (II) \((a,b,c,d)\) with \(b\ne a\), \(c\ne a\). For class I, a grain at position one yields \((a,a,a,d)\). Consequently, these last coordinates must be pairwise distinct and avoid \(D\); there are at most \(q-t\) such words. For class II, every fixed ordered pair \((b,c)\) admits at most one final coordinate \(d\), since a grain at position three maps every \((a,b,c,d)\) to the same \((a,b,c,c)\). There are only \((q-1)^2\) choices for \((b,c)\). Therefore
\[
|C_a|\le t+(q-t)+(q-1)^2=q^2-q+1.
\]
Summing over the \(q\) possible first symbols gives \(|C|\le q^3-q^2+q\). The argument includes the cases \(t=0\) and \(t=q\), and does not presume linearity.

**Attainment for \(q\ge3\).** The displayed \(C_L\) has exactly \(q[1+q(q-1)]\) words. Distinct first coordinates can never give a common output. Within a fixed first coordinate \(a\), the constant word \((a,a,a,a)\) cannot conflict with a constructed word \((a,b,c,L(b,c))\) having \(b\ne a\): every output of the latter still has second coordinate \(b\), except a possible overwrite of position one, which yields \((a,a,c,L(b,c))\). For that output to be constant would require \(c=a=L(b,a)\), contrary to the fact that the Latin column \(a\) already has its unique occurrence of symbol \(a\) in row \(a\).

Take two different nonconstant codewords \(x=(a,b,c,L(b,c))\) and \(y=(a,b',c',L(b',c'))\). If \(b\ne b'\), common outputs would necessarily arise from overwriting position one in both words, since otherwise the second output coordinates differ. Such a common output requires \(c=c'\) and \(L(b,c)=L(b',c)\), contradicting injectivity in column \(c\). If \(b=b'\), then \(c\ne c'\) and their last coordinates differ by injectivity in row \(b\). The only potential cross-type collision of the position-two and position-three overwrite outputs requires that one word have third coordinate \(b\), and the other have last coordinate \(b\). But idempotence gives \(L(b,b)=b\), and injectivity of the row says \(L(b,c)=b\) only if \(c=b\); hence those two conditions would force \(c=c'\), which is excluded. No original-output or same-type collision is possible because the relevant ordered-pair projections are injective. Therefore the output sets are pairwise disjoint.

**The binary exception.** The six words `0000`, `0011`, `0110`, `1001`, `1100`, `1111` have mutually disjoint grain-output sets by direct examination. The universal upper bound gives six for \(q=2\), completing the proof for all integers \(q\ge2\).

The only imported existence fact is the classical idempotent-Latin-square theorem for orders other than two. For odd \(q\ge3\) it can alternatively be made explicit without any existence theorem by taking \(Q=\mathbb Z/q\mathbb Z\) and \(L(b,c)=2b-c\pmod q\); both multiplication by \(2\) and by \(-1\) are invertible. For prime powers \(q\ge3\), the affine field expression \(L(b,c)=(1-\lambda)b+\lambda c\) with \(\lambda\notin\{0,1\}\) gives another explicit construction. The general composite even case uses the classical Latin-square existence theorem.

## Verification
`verify_latin_grain.py` independently constructs idempotent Latin squares by constraint propagation for orders \(3,4,5,6\), constructs the corresponding codes, and checks every received output for uniqueness. It separately checks the six-word binary construction. Verified code sizes are \(6,21,52,105,186\) at \(q=2,3,4,5,6\). `verify_modular_grain.cpp` implements the independent modular construction at odd alphabet sizes \(3,5,7,9,11\), checking code sizes \(21,105,301,657,1221\) and output uniqueness. Both programs have no external scientific datasets; they are finite consistency checks, while the preceding proof is for arbitrary finite \(q\).

## Relationship to prior work
The predecessor-overwrite grain channel, including arbitrary alphabet cardinality, is defined by Sharov and Roth [1], whose article develops rate bounds and binary finite-block constructions. Gabrys, Yaakobi and Dolecek [2] study related binary grain-error codes and nonbinary constituent codes. The exact length-four alphabet-uniform formula above, its projection upper bound, and its idempotent Latin-square attaining construction are not supplied by the compared full texts. The familiar six-word binary optimal value is not asserted to be new. The Latin-square existence theorem itself is classical, and is not asserted to be new [3].

## Limitations
This result is exact only for one overwrite of a following coordinate at blocklength four; no claim is made for multi-grain patterns, other lengths, alternative overwrite directions without coordinate reversal, or physical performance of multilevel magnetic recording. The original physical context is binary; general alphabets are a mathematical generalization. An equivalent unpublished or unindexed specialization cannot be excluded by bibliographic searching. Verification examples do not substitute for the all-alphabet proof. No independent mathematical audit has been carried out.

## References
[1] A. Sharov and R. M. Roth, *Bounds and Constructions for Granular Media Coding*, IEEE Transactions on Information Theory **60** (2014), 2010–2027, doi:10.1109/TIT.2014.2301811. Relevant full-text comparisons: introduction, Sections II, IV, V, and appendices.

[2] R. Gabrys, E. Yaakobi, and L. Dolecek, *Correcting Grain-Errors in Magnetic Media*, arXiv:1307.7087v1 (first posted 2013-07-26); see also IEEE Transactions on Information Theory **61** (2015), 2256–2272. The checked paper develops the binary single-grain model and its bounds.

[3] J. Allsop, *Cycles of quadratic Latin squares and antiperfect 1-factorisations*, Journal of Combinatorial Designs (2023), doi:10.1002/jcd.21905, Section 6 (states the classical existence of idempotent Latin squares in every order other than two).
