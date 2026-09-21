# Exact binary BCH minimum distance at s=6 and a period-seven distance-five family

Let
\[
N_s=2^{2s}+2^s+1=\frac{2^{3s}-1}{2^s-1},
\]
and let \(\mathcal C_s=\mathcal C_{(2,N_s,5,1)}\) denote the narrow-sense binary BCH code of length \(N_s\) and designed distance \(5\). Thus, for a primitive \(N_s\)-th root \(\beta\), every codeword polynomial vanishes at \(\beta,\beta^2,\beta^3,\beta^4\). In characteristic two it is enough to verify the roots \(\beta\) and \(\beta^3\).

## Result

**Theorem.**

1. For \(s=6\),
   \[
   \mathcal C_6\text{ has parameters }[4161,4125,6]_2.
   \]
2. If \(7\mid s\) and \(21\nmid s\), then
   \[
   d(\mathcal C_s)=5.
   \]
   In particular,
   \[
   \mathcal C_7\text{ has parameters }[16513,16471,5]_2.
   \]

The second statement supplies a period-seven sufficient class for exact distance five. It overlaps previously known sufficient classes for some values of \(s\), but adds uncovered cases; for example \(s=7,49,77,91\) are not in the congruence/divisibility classes of Wang--He--Yi--Zheng described below.

## Context

Wang, He, Yi and Zheng (2026) studied this same family and constructed weight-five codewords for several infinite classes, including \(s\equiv2,4\pmod 6\) and a class controlled by divisibility by \(5\). They also observed that the unrestricted distance-five assertion fails: for example, their paper records \(d(\mathcal C_3)=6\) and \(d(\mathcal C_1)=7\). The theorem above addresses two parameter regimes not resolved by those sufficient classes: it determines the exact value at \(s=6\), and gives an additional period-seven construction.

## Proof of the period-seven family

Set
\[
M=2^{14}+2^7+1=16513=49\cdot337.
\]
Then
\[
M=\frac{2^{21}-1}{2^7-1},
\]
so the multiplicative order of \(2\) modulo \(M\) divides \(21\); the verification artifact checks that it is exactly \(21\).

Work in
\[
\mathbb F_{2^{21}}=\mathbb F_2[t]/(t^{21}+t^2+1).
\]
The residue class of \(t\) is primitive. Put \(\theta=t^{127}\); since \((2^{21}-1)/M=127\), \(\theta\) has exact order \(M\). Direct field arithmetic gives the two identities
\[
1+\theta^{254}+\theta^{267}+\theta^{1729}+\theta^{2966}=0,
\]
\[
1+\theta^{762}+\theta^{801}+\theta^{5187}+\theta^{8898}=0.
\]
The second identity is the cube of the exponents in the first, so equivalently the binary polynomial with support
\[
E=\{0,254,267,1729,2966\}
\]
vanishes at both \(\theta\) and \(\theta^3\).

Now let \(s=7k\) with \(3\nmid k\). Modulo \(21\), \(s\) is either \(7\) or \(14\). Since \(2^{21}\equiv1\pmod M\), in either case
\[
N_s=2^{2s}+2^s+1\equiv2^{14}+2^7+1\equiv0\pmod M.
\]
Thus \(M\mid N_s\). Also \(21\mid3s\), so \(\mathbb F_{2^{21}}\) embeds in \(\mathbb F_{2^{3s}}\), which contains all \(N_s\)-th roots of unity.

Write \(D=N_s/M\). In the cyclic group of \(N_s\)-th roots one may choose a primitive root \(\beta\) with
\[
\beta^D=\theta.
\]
Indeed, if \(g\) generates the order-\(N_s\) group and \(\theta=(g^D)^a\) with \(\gcd(a,M)=1\), one can choose an integer \(a'\equiv a\pmod M\) avoiding every prime divisor of \(D\) not already dividing \(M\); then \(\gcd(a',N_s)=1\) and \(\beta=g^{a'}\) has the required properties. Therefore
\[
c(x)=\sum_{e\in E}x^{De}
\]
satisfies \(c(\beta)=c(\beta^3)=0\). Over \(\mathbb F_2\), Frobenius then gives the roots \(\beta^2\) and \(\beta^4\) as well, hence \(c\in\mathcal C_s\). The five exponents \(De\pmod{N_s}\) are distinct because the elements \(\theta^e\) are distinct. Thus \(c\) has weight five. The BCH bound gives \(d(\mathcal C_s)\ge5\), so equality follows.

For \(s=7\), \(N_7=M=16513\). The binary cyclotomic cosets of \(1\) and \(3\) modulo \(16513\) are disjoint and each have size \(21\). Hence the defining set has size \(42\), giving dimension \(16513-42=16471\).

## Exact computation for s=6

Here
\[
N_6=2^{12}+2^6+1=4161.
\]
Work in
\[
\mathbb F_{2^{18}}=\mathbb F_2[t]/(t^{18}+t^3+1).
\]
The element \(g=t^3+t\) is primitive. With
\[
\theta=g^{63},\qquad 63=\frac{2^{18}-1}{4161},
\]
\(\theta\) has exact order \(4161\).

The explicit support
\[
\{0,7,1801,2305,3181,3244\}
\]
satisfies
\[
\sum_e\theta^e=0,\qquad \sum_e\theta^{3e}=0,
\]
so it gives a weight-six codeword and hence \(d(\mathcal C_6)\le6\).

It remains to exclude weight five. By cyclically shifting any hypothetical weight-five codeword, assume that exponent \(0\) belongs to its support. Define
\[
v_e=(\theta^e,\theta^{3e})\in\mathbb F_{2^{18}}^2.
\]
If the other four distinct exponents are \(i,j,k,\ell\), the two BCH root equations are exactly
\[
v_i+v_j+v_k+v_\ell=v_0.
\]
Consequently some partition into two pairs satisfies
\[
v_i+v_j=(v_k+v_\ell)+v_0.
\]
The verification artifact exhaustively forms all unordered pairs from the \(4160\) nonzero exponents, sorts them by the pair syndrome \(v_i+v_j\), and checks for a complementary pair syndrome with disjoint indices. There are
\[
\binom{4160}{2}=8,650,720
\]
pairs. No disjoint complementary pair exists. This is exhaustive for weight five, not a random search.

The BCH bound already excludes weights below five, so the absence of weight five and the displayed weight-six codeword give
\[
d(\mathcal C_6)=6.
\]
Finally, the binary cyclotomic cosets of \(1\) and \(3\) modulo \(4161\) are disjoint and each have size \(18\), so
\[
\dim\mathcal C_6=4161-18-18=4125.
\]

## Reproducibility

`artifacts/verify_bch_period6_period7.cpp` is a standalone C++17 verifier using exact polynomial-basis arithmetic over binary fields. It checks:

- irreducibility of \(t^{18}+t^3+1\) and \(t^{21}+t^2+1\);
- the claimed primitive elements and exact orders of \(\theta\);
- the weight-six relation for \(s=6\);
- exhaustive nonexistence of a weight-five word for \(s=6\) by the pair-syndrome argument above;
- the weight-five period-seven relation;
- the relevant cyclotomic-coset sizes and dimensions for \(s=6\) and \(s=7\).

A reference invocation is

```text
g++ -O3 -std=c++17 artifacts/verify_bch_period6_period7.cpp -o verify_bch
./verify_bch
```

The expected output is recorded in `artifacts/verification.txt`.

## Limitations

The \(s=6\) lower bound is computer-assisted: it relies on a finite exhaustive enumeration whose completeness is justified by the pair-syndrome reduction above. The period-seven theorem is a sufficient family, not a classification of all \(s\) for which the minimum distance is five. The originality assessment is to the best of our knowledge; older BCH code tables, theses, or computational catalogues that are poorly indexed remain a residual coverage risk.

## Reference

X. Wang, J. He, B. Yi, and D. Zheng, *Solutions to Three Conjectures and an Open Problem on Binary BCH Codes*, arXiv:2609.00532 (2026).
