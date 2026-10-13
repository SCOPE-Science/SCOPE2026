# The shortest \(\{3,5,11\}\)-smooth Egyptian representation of one has 17 terms

## Finding

Define \(S=\{3^a5^b11^c:a,b,c\in\mathbb{Z}_{\ge0}\}\). A restricted Egyptian representation is an identity
\[
1=\sum_{i=1}^k\frac{1}{d_i},\qquad 1<d_1<d_2<\cdots<d_k,\quad d_i\in S.
\]
The smallest possible length is **exactly \(k=17\)**. An explicit strictly increasing witnessing tuple is
\[
(3,5,9,11,15,25,27,33,45,55,75,81,99,125,225,891,1125).
\]

## Assumptions and scope

All exponents defining \(S\) are nonnegative integers. Denominators are positive, greater than one, and pairwise distinct; there is no upper bound on their sizes. The assertion is an exact minimum over all such finite representations, not a count or uniqueness classification of all representations of length \(17\).

The support \(\{3,5,11\}\) is the next admissible set after \(\{3,5,7\}\) in the classical family \(\{3,5,p\}\) with \(p>5\) prime: the known feasibility inequality is \(\frac32\frac54\frac p{p-1}>2\), equivalent to \(p<16\). Hence \(p\in\{7,11,13\}\) are precisely the admissible cases in this family. Feasibility itself is prior work; the minimum \(17\) for \(p=11\) is the finding.

## Proof

**Order bound.** Write the elements of \(S\setminus\{1\}\) in increasing order, \(s_1<s_2<\cdots\). The first sixteen are exactly
\[
3,5,9,11,15,25,27,33,45,55,75,81,99,121,125,135.
\]
This follows by listing all products of powers of \(3,5,11\) at most \(135\). Exact rational addition gives
\[
\sum_{i=1}^{14}\frac1{s_i}=\frac{243508}{245025}<1,
\qquad
\sum_{i=1}^{15}\frac1{s_i}=\frac{1227341}{1225125}>1.
\]
The first expression proves impossibility for every \(k\le14\), because the smallest \(k\) denominators always maximize the sum of \(k\) distinct reciprocals from \(S\).

**Fifteen terms.** Suppose a 15-term representation exists. It must contain all of \(s_1,\ldots,s_{13}\). Indeed, omitting any one of these terms reduces even the *largest conceivable* fifteen-reciprocal sum to at most
\[
\sum_{i=1}^{15}\frac1{s_i}-\frac1{99}+\frac1{135}
=\frac{1224041}{1225125}<1.
\]
The last two denominators, \(x<y\), are therefore distinct elements of \(S\) exceeding \(99\) and satisfy
\[
\frac1x+\frac1y=1-\sum_{i=1}^{13}\frac1{s_i}=\frac{322}{22275}.
\]
Since \(x<y\), we have \(\frac1x+\frac1y<\frac2x\), hence \(x<\frac{22275}{161}<139\). The only eligible \(S\)-smooth integers in \((99,139)\) are \(121,125,135\). Solving the exact equation for the second denominator gives respectively
\[
 y=\frac{245025}{1517},\qquad
 y=\frac{111375}{719},\qquad
 y=\frac{22275}{157}.
\]
None is an integer (each displayed fraction has nonzero residue modulo its denominator). Thus \(k=15\) is impossible.

**Parity.** Every member of \(S\) is odd. Multiplying any purported representation by the odd least common multiple \(L\) of its denominators gives \(L=\sum_i L/d_i\). Every summand is odd, so \(k\) must be odd. In particular \(k=16\) is impossible.

**Attainment.** For the 17 displayed denominators the least common multiple is \(111375\). The corresponding integer numerators \(111375/d_i\) are
\[
37125,22275,12375,10125,7425,4455,4125,3375,2475,2025,1485,1375,1125,891,495,125,99.
\]
They sum to exactly \(111375\), so their reciprocals sum to \(1\). All denominators are distinct products of powers of \(3,5,11\). Combining the obstructions and the witness proves the minimum is \(17\).

## Verification

The accompanying `verify_egyptian.py` uses exact integer and rational arithmetic. It reconstructs the first sixteen smooth denominators by a complete bounded exponent sieve, checks the exact reciprocal sums and mandatory-prefix bound, checks all three fifteen-term residual cases without rounding, and verifies the 17-term identity and support restriction. Execute with `python3 verify_egyptian.py`. Computation only checks the finite certificates; the preceding argument establishes the unbounded minimum.

## Relationship to prior work

Chen, Elsholtz and Jiang [1] define the restricted representation counts \(T_k(p_1,\ldots,p_t)\), prove the general reciprocal-sum feasibility criterion, and treat existence and growth along progressions. They quote Burshtein's count of **seventeen different representations of length eleven** for support \(\{3,5,7\}\); this is a different invariant and a different prime support from the **minimal length seventeen** proved here. The inspected statements of [1] do not give the minimum for \(\{3,5,11\}\), and [2] studies only \(\{3,5,7\}\). The proof here is elementary and self-contained.

## Limitations

This is a minimum-length result only for exact support contained in \(\{3,5,11\}\), with distinct denominators. It does not enumerate all shortest representations, determine other supported length sets, or give the minimum for \(\{3,5,13\}\). An equivalent result could exist in literature not indexed by the cited searches.

## References

[1] Y.-G. Chen, C. Elsholtz and L.-L. Jiang, *Egyptian Fractions with Restrictions*, arXiv:1108.6118v1 (first posted 31 August 2011), *Acta Arithmetica* 154 (2012), 109–123. https://arxiv.org/html/1108.6118v1

[2] N. Burshtein, *All the solutions of the equation \(\sum_{i=1}^{11}1/x_i=1\) in distinct integers of the form \(x_i\in3^\alpha5^\beta7^\gamma\)*, *Discrete Mathematics* 308 (2008), 4286–4292. DOI:10.1016/j.disc.2007.08.049.
