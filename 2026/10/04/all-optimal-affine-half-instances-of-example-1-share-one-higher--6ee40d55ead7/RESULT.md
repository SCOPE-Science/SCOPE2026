# All optimal affine-half instances of Example 1 share one higher-support spectrum
## Finding

Chung--Jin--Kim Example 1 takes
\[
m=6,\qquad t=3,\qquad r=2,
\]
and for an affine normal outside the relevant dual-spread union obtains an optimal affine-half code with parameters
\[
[95,7,22]_2.
\]

In the explicit Desarguesian model
\[
\mathbb F_2^6\cong\mathbb F_8^2,
\]
there are \(9\) spread components. Choosing \(2\) of them gives
\[
\binom{9}{2}=36
\]
possible partial spreads. For each such pair, the source's outside-normal condition leaves
\[
49
\]
nonzero normals. Hence there are
\[
36\cdot49=1764
\]
optimal-normal instances in this model.

Every one of these \(1764\) codes has the same generalized Hamming-weight hierarchy:
\[
(d_1,d_2,d_3,d_4,d_5,d_6,d_7)
=
(22,56,74,84,90,93,95).
\]

More strongly, all \(1764\) codes have the same complete support-size spectrum in every subcode dimension. For \(s=1\),
\[
22:1,\ 42:12,\ 46:36,\ 48:62,\ 54:3,\ 58:12,\ 64:1.
\]
For \(s=2\),
\[
56:12,\ 58:36,\ 62:2,\ 64:12,\ 66:66,\ 68:432,\ 70:613,\ 72:656,\ 74:240,\ 76:432,\ 78:20,\ 80:67,\ 82:78,\ 86:1.
\]
For \(s=3\),
\[
\begin{aligned}
&74:36,\ 75:144,\ 76:102,\ 77:24,\ 78:114,\ 79:288,\ 80:696,\ 81:1360,\\
&82:1062,\ 83:864,\ 84:2920,\ 85:1376,\ 86:442,\ 87:864,\ 88:1067,\\
&89:48,\ 90:228,\ 91:144,\ 92:18,\ 93:8,\ 94:6.
\end{aligned}
\]
For \(s=4\),
\[
84:144,\ 85:180,\ 86:552,\ 87:908,\ 88:1464,\ 89:1616,\ 90:2713,\ 91:1520,\ 92:1679,\ 93:668,\ 94:267,\ 95:100.
\]
For \(s=5\),
\[
90:256,\ 91:240,\ 92:567,\ 93:748,\ 94:548,\ 95:308.
\]
For \(s=6\),
\[
93:32,\ 94:31,\ 95:64,
\]
and for \(s=7\),
\[
95:1.
\]

Here the notation \(w:N\) means that exactly \(N\) subcodes of the stated dimension have support size \(w\).

## Assumptions and scope

The field is represented as
\[
\mathbb F_8=\mathbb F_2[z]/(z^3+z+1).
\]
The Desarguesian spread consists of
\[
E_\lambda=\{(x,\lambda x):x\in\mathbb F_8\},
\qquad
E_\infty=\{(0,x):x\in\mathbb F_8\}.
\]
The standard coefficient-vector dot product on \(\mathbb F_2^6\) is used.

For each unordered pair \(E_i,E_j\), let \(f\) be the indicator of
\[
(E_i\cup E_j)\setminus\{0\}.
\]
Let
\[
\mathcal U=E_i^\perp\cup E_j^\perp.
\]
For each
\[
a\in\mathbb F_2^6\setminus\mathcal U,
\]
the code is the source affine-half code
\[
\mathcal R_{f,a}
=
\left\{
\left(uf(x)+\langle v,x\rangle\right)_{x\in V^\ast}
\parallel
\left(uf(x)+\langle v,x\rangle\right)_{x\in A_a}
:
u\in\mathbb F_2,\ v\in V
\right\},
\]
where
\[
A_a=\{x:\langle a,x\rangle=1\}.
\]

The claim is finite and exact for this explicit \(m=6\), \(r=2\) Desarguesian model. It does not assert the same higher-support spectrum for the \(m=8\), \(r=4\) example or for arbitrary partial spreads not equivalent to this model.

## Proof

The source proves that in the \(m=6\), \(r=2\) case every normal outside \(\mathcal U\) gives an affine-half-optimal \([95,7,22]_2\) code. In the explicit Desarguesian spread there are \(36\) component pairs. Each dual-spread union has
\[
1+2(8-1)=15
\]
vectors, so among the \(63\) nonzero normals exactly
\[
63-14=49
\]
are outside.

For a fixed component pair and outside normal, a generator matrix has \(7\) rows. Its first \(63\) columns are
\[
(f(x),x)^{\mathsf T},
\qquad x\in V^\ast,
\]
and the \(32\) positions with \(\langle a,x\rangle=1\) are duplicated, giving length \(95\).

An \(s\)-dimensional subcode is the image of an \(s\)-dimensional subspace of the \(7\)-dimensional message space. Every such message subspace has a unique reduced-row-echelon representative. The numbers of subspaces in dimensions \(1\) through \(7\) are
\[
127,\ 2667,\ 11811,\ 11811,\ 2667,\ 127,\ 1.
\]
For each representative basis, the union of the supports of its basis images is exactly the support of the whole subcode.

The exhaustive computation performs this support calculation for every subspace for every one of the \(1764\) optimal-normal instances. Thus it checks
\[
1764\cdot29211=51528204
\]
subcode instances. The resulting support histogram is identical in every case. Taking the smallest support in each dimension gives
\[
(22,56,74,84,90,93,95).
\]

The \(s=1\) spectrum is
\[
22:1,\ 42:12,\ 46:36,\ 48:62,\ 54:3,\ 58:12,\ 64:1,
\]
which exactly reproduces the source's published Example 1 weight enumerator. This independently anchors the implementation to the source construction before the higher-dimensional census is used.

## Verification

`artifacts/verify.py` uses only the Python standard library.

It constructs \(\mathbb F_8\) from \(z^3+z+1\), builds all \(9\) Desarguesian spread components, forms their orthogonal complements, and loops over all \(36\) component pairs and all \(49\) outside normals for each pair.

For every code it constructs the exact \(7\times95\) binary generator matrix. It then enumerates every message subspace in reduced row-echelon form and computes the support of the corresponding subcode. The replay checks that all \(1764\) instances have one identical complete support spectrum and the hierarchy
\[
(22,56,74,84,90,93,95).
\]
It also checks that the one-dimensional spectrum equals the source's published weight enumerator.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Chung--Jin--Kim determine the complete ordinary weight distributions of the affine-half family and prove that, for \(2\le r\le 2^{t-2}\), the outside-normal condition is exactly the affine-half minimum-distance optimum. For Example 1 they explicitly give the outside-normal \([95,7,22]_2\) weight enumerator.

Their article does not state generalized Hamming weights or higher-dimensional subcode-support distributions. Exact searches for \([95,7,22]_2\) together with generalized-Hamming terminology, for the hierarchy
\[
(22,56,74,84,90,93,95),
\]
and for affine-half or partial-spread higher-support formulations did not locate a prior statement of this spectrum.

Earlier work on partial-spread minimal codes establishes minimality and ordinary-weight behavior of parent constructions, but does not imply the support unions of higher-dimensional subcodes after the affine-half coordinate duplication. The present result therefore refines the source's ordinary weight and minimum-distance analysis in a direction not determined by its published enumerators.

## Limitations

The result is an exact finite classification inside the source's explicit \(m=6\), \(r=2\) Desarguesian model. It is not a proof that all affine-half codes with the same parameters outside this model are equivalent.

The computation shows higher-support isospectrality, not coordinate-permutation equivalence. Distinct instances may still differ under finer invariants.

No general closed formula for arbitrary \(m\) and \(r\) is claimed.

## References

1. Jin-Ho Chung, Dongsup Jin, and Daehwan Kim, *Affine-Half Extensions of Partial-Spread Minimal Binary Linear Codes with Explicit Weight Distributions*, Mathematics 14 (2026), 3152, DOI 10.3390/math14173152.
2. Cunsheng Ding, Zhengchun Heng, and Zhengchun Zhou, *Minimal binary linear codes*, IEEE Transactions on Information Theory 64 (2018), 6536--6545.
3. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418.
