# Exact additive and Abelian four-power order spectra of the Tribonacci word through \(1705\)

## Finding

Let \(\tau\) be the infinite fixed point beginning with \(0\) of the substitution
\[
\mu(0)=01,\qquad \mu(1)=02,\qquad \mu(2)=0.
\]
For \(d\geq1\), call \(d\) an **additive four-power order** if some factor of \(\tau\) of length \(4d\) has a decomposition \(B_0B_1B_2B_3\), each \(B_j\) of length \(d\), with equal digit sums. It is an **Abelian four-power order** if instead all four blocks have equal Parikh vectors (counts of the symbols \(0,1,2\)).

**Theorem (finite exact order spectra).** For every integer \(1\leq d\leq1705\), the presence or absence of each kind of four-power is specified exactly in `data/additive_orders.csv` and `data/abelian_orders.csv`. In this interval there are precisely **579 additive orders**, **462 Abelian orders**, and **117 additive orders that are not Abelian orders**. The least additive order and the least Abelian order are both \(6\). Their first separation is \(d=10\): additive four-powers occur at this order but Abelian four-powers do not.

The complete cumulative counts at the natural substitution-length cutoffs are:

| Maximum order \(d\) | Additive | Abelian | Additive but not Abelian |
|---:|---:|---:|---:|
| 7 | 2 | 2 | 0 |
| 13 | 5 | 4 | 1 |
| 24 | 8 | 7 | 1 |
| 44 | 13 | 11 | 2 |
| 81 | 28 | 22 | 6 |
| 149 | 49 | 41 | 8 |
| 274 | 88 | 72 | 16 |
| 504 | 169 | 136 | 33 |
| 927 | 311 | 250 | 61 |
| 1705 | 579 | 462 | 117 |

The two included CSVs are complete classifications, not samples. Each has exactly one row per \(d\in\{1,\ldots,1705\}\), with columns `d,pair,index`. For a positive order, `pair` is a length-two factor of \(\tau\) and `index` is the starting offset of a valid length-\(4d\) witness in \(\mu^{16}(\text{pair})\). For an absent order, the fields are `none,-1`; its absence is certified by the finite-cover proof below. Here \(\mu^{16}(xy)\) means \(\mu^{16}(x)\mu^{16}(y)\).

## Assumptions and scope

The symbols are literal integers \(0,1,2\), so the sum in the definition is the sum of these integer values. All four blocks are contiguous and have equal **positive** length. Their common order \(d\) is bounded by \(1705=|\mu^{12}(0)|\). A witness can begin anywhere in the one-sided infinite word \(\tau\), not just in its initial prefix.

The only level-two factors of \(\tau\) are
\[
\mathcal D=\{00,01,02,10,20\}.
\]
Write \(U_x=\mu^{16}(x)\). Their lengths are
\[
|U_0|=19513,\qquad |U_1|=16377,\qquad |U_2|=10609.
\]
In particular, \(4\cdot1705=6820<10609\). No assertion is made about any order \(d>1705\).

## Proof

**Step 1: exact adjacent-block cover.** Every substitution image starts with \(0\), and the last symbols of \(\mu(0),\mu(1),\mu(2)\) are respectively \(1,2,0\). Internal adjacent pairs of images are \(01\) and \(02\); boundary pairs belong to \(\{10,20,00\}\). Each symbol occurs in \(\tau\), and each image boundary occurs since \(\tau\) is infinite. This establishes the displayed exact digram set \(\mathcal D\).

Because \(\tau=\mu^{16}(\tau)\), every position belongs to one level-sixteen image \(U_x\) within the natural concatenation. Every interval of length at most \(6820\), beginning anywhere within that image, ends before the end of the immediately following image: all images are longer than \(6820\). Thus every factor of \(\tau\) of length at most \(6820\) is included in \(U_xU_y\) beginning at an offset \(0\leq i<|U_x|\), for some \(xy\in\mathcal D\). Conversely every such two-image word occurs as an image of an actual digram of \(\tau\). This provides an **if and only if** infinite-word-to-finite-cover reduction, valid uniformly for every \(1\leq d\leq1705\).

**Step 2: integer test of both predicates.** For each pair \(xy\in\mathcal D\), form prefix counts \(P_0,P_1\) of symbols \(0\) and \(1\) in \(U_xU_y\). For \(j\in\{0,1,2,3\}\), let
\[
(a_j,b_j)=\bigl(P_0(i+(j+1)d)-P_0(i+jd),\;P_1(i+(j+1)d)-P_1(i+jd)\bigr).
\]
The count of \(2\) in that block is \(d-a_j-b_j\), and hence its digit sum is
\[
2d-2a_j-b_j.
\]
Consequently the four blocks are Abelian-equivalent exactly when all \((a_j,b_j)\) are identical, and additively equivalent exactly when all \(2a_j+b_j\) are identical. These are necessary and sufficient integer equality tests, with no probabilistic or floating-point computation.

**Step 3: complete finite exhaustion.** For every \(d=1,2,\ldots,1705\), scan all \(xy\in\mathcal D\) and all offsets \(0\leq i<|U_x|\), evaluating both exact tests from Step 2. Record whether either property appears and, if so, one first encountered `(pair,index)` witness. The two CSV files contain the full resulting membership functions, positive witnesses, and explicit negative rows. The five-image-pair cover from Step 1 proves every negative row, while Step 2 proves every positive row. Counting the two membership columns gives \(579\) and \(462\); their difference gives \(117\) because Abelian equality implies additive equality.

For illustration, the four blocks at the first strict-separation order \(d=10\) can be taken as

```
0010201020  1001020101  0201001020  1001020101
```

Each has digit sum \(6\), but their Parikh vectors alternate between \((6,2,2)\) and \((5,4,1)\). The exhaustive cover rules out **any** Abelian four-power of order \(10\) at another starting position.

## Verification

The included standalone `verify.py` uses only Python's standard library and the two CSV files. Run from this directory:

```
python3 verify.py
```

It checks every CSV row and all positive fixed-level-sixteen witnesses, independently regenerates each membership bit by scanning a separate **minimal sufficient substitution level** for that \(d\), compares all \(3410\) yes/no decisions, checks the first strict separation and each displayed cutoff, and prints:

```
VERIFY_OK additive=579 abelian=462 additive_only=117 cutoff=1705
```

The verifier is a finite exact computation. The argument that it decides the infinite-word property is the adjacent-block cover proved above, **not** a heuristic extrapolation from a long prefix. The supplied CSVs and script are sufficient for offline reproduction.

## Relationship to prior work

Popoli, Shallit and Stipulanti (arXiv:2410.02409v1, October 3, 2024), Section 6, Theorems 36–37 and Problem 38, determine Abelian squares at all orders and automatic recognizers for **Abelian and additive cubes**, then explicitly raise the characterization of additive \(k\)-power orders in the Tribonacci word. They note computational difficulty for \(k=4\). The present statement concerns the specific finite interval of fourth-power orders and gives both the additive and Abelian membership tables; it does not claim a general automaton or resolve their all-order Problem 38.

Currie, Mol, Rampersad and Shallit (arXiv:2111.07857) construct an **other** morphic word avoiding Abelian fourth powers; their avoidance theorem does not classify the order spectrum of this Tribonacci fixed point. Turek's study of Tribonacci Abelian **factor complexity** counts Parikh classes of individual factors, which is different from four consecutive blocks falling in a common class. Couvreur et al. (arXiv:2504.13584), notably Theorems 19–23, prove automaticity and balancedness properties of **generalized factor-complexity functions** in the same Tribonacci word, but their inspected statements provide neither a four-consecutive-block order classifier nor the two finite membership tables here. OEIS A345717 and A347752 describe orders of **cubes**, not fourth powers. An equivalent fourth-power table not indexed in the consulted sources remains possible.

## Limitations

- The exact classification is restricted to \(1\leq d\leq1705\); it does not characterize all fourth-power orders, prove periodicity, or yield an asymptotic density.
- The numerical counts are part of an exhaustive finite algorithm, backed by a separate coverage proof; they are not a closed-form infinite classification.
- The literature comparison cannot exclude unpublished or unindexed equivalent computations. Independent scientific validation has not been performed.

## References

1. Pierre Popoli, Jeffrey Shallit and Manon Stipulanti, *Additive word complexity and Walnut*, arXiv:2410.02409v1 (first posted October 3, 2024), especially Section 6, Theorem 37 and Problem 38. https://arxiv.org/abs/2410.02409
2. James Currie, Lucas Mol, Narad Rampersad and Jeffrey Shallit, *Extending Dekking's construction of an infinite binary word avoiding abelian 4-powers*, arXiv:2111.07857v1 (November 15, 2021). https://arxiv.org/abs/2111.07857
3. Ondřej Turek, *Abelian Complexity Function of the Tribonacci Word*, Journal of Integer Sequences 18 (2015). https://cs.uwaterloo.ca/journals/JIS/VOL18/Turek/turek3.pdf
4. OEIS A345717, *Orders of abelian cubes in the tribonacci word*. https://oeis.org/A345717
5. OEIS A347752, *Orders of additive cubes in the tribonacci word*. https://oeis.org/A347752
6. Jean-Michel Couvreur, Martin Delacourt, Nicolas Ollinger, Pierre Popoli, Jeffrey Shallit and Manon Stipulanti, *Effective Computation of Generalized Abelian Complexity for Pisot Type Substitutive Sequences*, arXiv:2504.13584v2 (April 22, 2025), especially Theorems 19–23. https://arxiv.org/abs/2504.13584
