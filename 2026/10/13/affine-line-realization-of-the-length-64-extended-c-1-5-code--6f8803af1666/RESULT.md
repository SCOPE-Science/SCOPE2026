# Affine-line realization of the length-64 extended \(C_{1,5}\) code

## Finding
Let \(E\) denote the binary extended cyclic code \(C_{1,5}^*\) for \(m=6\), with coordinates indexed by the \(64\) elements of \(\mathbb F_{64}\). Then **\(E\) is exactly the binary code spanned by the incidence vectors of the affine lines of \(\operatorname{AG}(3,4)\)**, upon identifying \(\mathbb F_{64}\) with a three-dimensional vector space over its subfield \(\mathbb F_4\). This is an equality in the specified coordinate labeling, not just a parameter match.

The complete set of minimum-weight supports comprises the \(336\) distinct affine four-point lines. Their indicator vectors have rank \(51\), which is the dimension of \(E\). Thus the classical incidence code appearing in earlier work on quasi-symmetric designs is the \(m=6\) member of the 2026 extended \(C_{1,5}\) construction. Established consequences for the classical line code, including its semiaffine coordinate group, transfer to this instance; those previously known consequences are not claimed as independently new.

## Assumptions and scope
Work over \(\mathbb F_{64}=\mathbb F_2[\alpha]\), where \(\alpha\) is a root of the primitive polynomial \(T^6+T+1\). Let \(\omega=\alpha^{21}\), so \(\mathbb F_4=\{0,1,\omega,\omega^2\}\). Let the extended code consist of exactly those binary arrays \(c=(c_x)_{x\in\mathbb F_{64}}\) satisfying
\[
\sum_x c_x=0,\qquad \sum_x x c_x=0,\qquad \sum_x x^5c_x=0.
\]
The first equation is in \(\mathbb F_2\); the latter two are in \(\mathbb F_{64}\). Their simultaneous expansion over \(\mathbb F_2\) gives \(13\) parity equations. The labeling by field elements identifies this code with the parity extension of the primitive binary cyclic code with check zeros at exponents \(1\) and \(5\). The statement is restricted to \(m=6\): no geometric identification or automorphism result for other exponents or values of \(m\) is asserted.

For \(a\in\mathbb F_{64}\) and \(v\in\mathbb F_{64}^{\times}\), define the affine line \(L(a,v)=\{a+tv:t\in\mathbb F_4\}\). The vector \(1_L\) has coordinate \(1\) exactly on \(L\). Equal lines are counted once.

## Proof
**Field and code dimensions.** The powers of \(\alpha\) have order \(63\), and its Frobenius cyclotomic orbits at exponents \(1\) and \(5\) are disjoint, each of size \(6\). Consequently the two field-valued checks impose \(12\) independent binary constraints; the added overall parity is an independent thirteenth constraint. Equivalently, an explicit \(13\)-by-\(64\) binary parity-check matrix has rank \(13\) in the attached verifier, so \(\dim_{\mathbb F_2}E=51\).

**Every affine line belongs to \(E\).** For \(L(a,v)\), the parity check vanishes because it contains four points. Furthermore, in characteristic two \(\sum_{t\in\mathbb F_4}t=\sum_{t\in\mathbb F_4}t^2=0\) and \(t^4=t\). Thus \(\sum_t(a+tv)=0\), and expanding \((a+tv)^5=a^5+a^4vt+a(vt)^4+(vt)^5\) shows \(\sum_t(a+tv)^5=0\). Hence the line incidence span \(B\) satisfies \(B\subseteq E\).

**All minimum supports are affine lines.** The overall parity eliminates odd nonzero weights; two distinct coordinate values cannot satisfy the first moment check, so the minimum weight is at least four. Suppose \(\{a,a+s,c,c+s\}\) is a four-point support satisfying the two moment checks with \(s\ne0\). The fifth-power equation simplifies to
\[
s(a+c)^4+s^4(a+c)=0,
\]
so \(t=(a+c)/s\) satisfies \(t^4=t\), hence \(t\in\mathbb F_4\). Distinctness forces \(t\in\{\omega,\omega^2\}\). Therefore the support is precisely \(a+s\mathbb F_4\). Conversely, every such support is in the code. There are \((64-1)/3=21\) directions and \(64/4=16\) lines per direction, giving \(336\) distinct supports.

**Span equals the entire code.** In the explicit polynomial basis of the field, construct each line incidence vector as a 64-bit binary integer. Gaussian elimination over \(\mathbb F_2\) on all \(336\) vectors gives exactly \(51\) pivots, as reproduced deterministically by `verify.py`. Thus \(\dim B=51=\dim E\). Together with \(B\subseteq E\), this proves the stated equality \(B=E\).

**Previously known symmetry interpreted.** Because the minimum-weight supports are exactly the affine lines and they span \(E\), the coordinate-permutation group of \(E\) is precisely the affine-line collineation group. The fundamental theorem of affine geometry in dimension three identifies it as \(\operatorname{A\Gamma L}(3,4)\), of order \(64(64-1)(64-4)(64-16)\cdot2=23{,}224{,}320\). The 2016 affine-geometry code literature had already determined this collineation group; its transfer is a consequence of the new cross-description equality and is not an original group classification.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter. The fully contained script implements multiplication modulo \(T^6+T+1\), constructs the subfield, enumerates all \(336\) affine lines and their \(2016\) pairs, builds the full \(13\)-check matrix, computes its rank and the incidence-row rank, and independently exhausts every four-point zero-syndrome support via equal pair syndromes. Expected concluding diagnostics are `PARITY_CHECK_RANK 13`, `AFFINE_LINES 336`, `WEIGHT_FOUR_SUPPORTS 336`, `LINE_SPAN_RANK 51`, and `VERIFY_OK`. No floating-point arithmetic or external dependency is used.

## Relationship to prior work
Rifà and Zinoviev (2026, Proposition 3.5 and Section 3) construct the extended \(C_{1,5}\) family and prove its length, dimension, minimum distance and complete regularity. They analyze four-syndrome completions (Proposition 3.2) and affine invariance, but do not identify the \(m=6\) extended code with the \(\operatorname{AG}(3,4)\) line-incidence code. They note an intersection-array coincidence with earlier distance-regular graphs, which is strictly weaker than code equality.

Crnković, Rodrigues, Rukavina and Tonchev (2016, Section 1) studied the binary line-incidence code of \(\operatorname{AG}(3,4)\), reported its dimension \(51\) from Hamada's formula, and stated its full collineation automorphism group. The older line code, its rank, its group and their quasi-symmetric-design classification were already known. The present point is the explicit identification of the *recent cyclic-description code* with that already studied geometric code, established by checking its defining Fourier-zero equations and the full line span, not merely matching \([64,51,4]\) parameters.

## Limitations
This finding concerns only the \(m=6\) code. It does not establish a new generalized automorphism theorem or rediscover the historical incidence-rank theorem. A search of public literature cannot rule out an unindexed earlier statement of the precise equivalence. The computation is a finite exact rank calculation with a complete included algorithm, not a machine-checked formal proof in an external prover. The cited 2016 classification transfers only to its stated classical code and only via the proven equality.

## References
1. J. Rifà and V. Zinoviev, *Cyclic completely regular codes \(C_{1,5}\)*, *Designs, Codes and Cryptography* 94, article 105 (2026), first published 2026-05-09, DOI: 10.1007/s10623-026-01860-8.
2. D. Crnković, B. G. Rodrigues, S. Rukavina and V. D. Tonchev, *Classification of quasi-symmetric 2-(64,24,46) designs of Blokhuis-Haemers type*, arXiv:1602.05446 (first posted 2016-02-17), especially Section 1.
3. N. Hamada, *On the p-rank of the incidence matrix of a balanced or partially balanced incomplete block design and its application to error correcting codes*, Hiroshima Math. J. 3 (1973), 153–226 (cited for the classical geometric-rank background; the current finite rank is independently reconstructed).
