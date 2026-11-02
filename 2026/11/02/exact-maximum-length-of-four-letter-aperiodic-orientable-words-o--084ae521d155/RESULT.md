# Exact maximum length of four-letter aperiodic orientable words of span four

## Finding
For the alphabet \(\Sigma=\{0,1,2,3\}\), the longest finite word whose length-four factors are all distinct even when read backwards has exactly \(113\) letters. Equivalently, the greatest number of consecutive length-four windows in a noncyclic, reversal-free word is \(110\). In particular, writing \(L_{4}(4)\) for this finite-word maximum,
\[
L_{4}(4)=113.
\]
One optimal word, encoded with symbols \(0,1,2,3\), is

```text
11120010223001301320111303210003121101030020121201330202103231220230213101222030332113221231311033312320313323222
```

## Assumptions and scope
A finite word \(w=w_0\cdots w_{L-1}\in\Sigma^L\), with \(L\geq4\), is *aperiodically orientable of span four* when all \(2(L-3)\) words
\[
w_iw_{i+1}w_{i+2}w_{i+3},\qquad
w_{i+3}w_{i+2}w_{i+1}w_i\quad(0\leq i\leq L-4)
\]
are distinct. This excludes palindromic windows, repeats, and pairs of reversed windows. No cyclic wraparound windows are included. The result concerns all such words, without any restriction on the endpoints or on their factor graph being strongly connected.

## Proof
**Lower bound.** The displayed word has \(113\) letters. Its \(110\) consecutive four-letter factors are nonpalindromic, mutually distinct and pairwise non-reversals. The supplied `verify.py` independently checks all \(110\) factors as strings, so \(L_4(4)\geq113\).

**Upper-bound reduction.** Form the directed order-three de Bruijn graph with the \(64\) vertices \(v\in\Sigma^3\). Each four-letter word \(e\in\Sigma^4\) is a directed edge from its three-letter prefix to its three-letter suffix. Exactly \(16\) four-letter words are palindromes, leaving \(240\) allowed edges, partitioned into \(120\) unordered reversal pairs \(\{e,e^R\}\). For each allowed edge introduce a binary variable \(x_e\), and for each vertex introduce binary source and terminal variables \(s_v,t_v\). Consider the following finite binary optimization problem:
\[
\begin{aligned}
\text{maximize }&\sum_e x_e,\\
\sum_{e:\operatorname{tail}(e)=v}x_e-
\sum_{e:\operatorname{head}(e)=v}x_e&=s_v-t_v &&(v\in\Sigma^3),\\
x_e+x_{e^R}&\leq1 &&(\{e,e^R\}\text{ a reversal pair}),\\
\sum_v s_v=\sum_v t_v&=1,\\
x_e,s_v,t_v&\in\{0,1\}.
\end{aligned}
\]
Any permissible finite word of length \(L\) traces a directed trail using exactly \(L-3\) selected distinct edges; its edge-incidence vector satisfies the pair constraints, and its first and last three-letter factors supply the required \(s,t\). This is true even when the endpoints coincide. Hence the optimum of this relaxation (which **does not require connectivity**) is an upper bound on \(L-3\).

**Finite integer optimum.** The explicit optimization has \(368\) binary variables, \(64\) flow equalities, \(120\) reversal inequalities and \(2\) endpoint-count equalities. Exact coefficients and the complete construction of every row are contained in `verify.py`. Solving the stated integer program with SciPy's HiGHS mixed-integer solver at zero requested relative MIP gap returns objective \(110\), dual bound \(110\), status optimal and zero reported gap. The standalone replay checks those outputs, every integer constraint on the returned optimizer, and an independently constructed feasible assignment from the displayed word. Thus the computational upper certificate is \(L-3\leq110\), which meets the displayed lower witness and yields \(L\leq113\). This finite optimization step is computationally certified by the named solver; it is not presented as a separately formalized or solver-independent symbolic inequality.

## Verification
Run `python verify.py` in an environment providing NumPy and SciPy with the HiGHS mixed-integer backend. The script generates the \(240\) allowed edges and \(120\) reversal pairs from first principles, constructs the \(186\)-row binary integer program, independently verifies the literal word as well as the optimized binary vector using integer arithmetic, and requires the solver's optimal primal and dual bounds to agree at \(110\). It prints `QUATERNARY_APERIODIC_ORIENTABLE_4_VERIFY_OK`. No unpublished data, precomputed solver solution or external code repository is needed. Numerical MIP bound certification depends on the correctness of the optimization backend; independent formal proof of the upper bound has not been performed.

## Relationship to prior work
Mitchell (2026, arXiv:2610.33601v1) derives finite and periodic extremal lengths for the *binary* alphabet and introduces a related de Bruijn graph integer-programming method. The present statement instead fixes four symbols and four-letter windows and solves the *aperiodic* maximum. Mitchell and Wild (2025 preprint, 2026 journal article) address periodic, nonbinary orientable sequences, including order four; these periodic results do not directly determine the finite maximum. Gabrić and Sawada (2024) provide general cyclic constructions and note the passage to finite sequences by unwrapping one period and adjoining three terminal letters, but such a construction is not an upper bound for general finite sequences. The finite endpoint relaxation and its exact optimum are distinct from periodic period constructions, which yield only some aperiodic examples when unwrapped.

## Limitations
The theorem covers precisely the four-symbol, four-window, noncyclic setting. It neither classifies all maximizing words nor supplies a formula in general alphabet size or span. The upper bound is reconstructed by an executable integer-optimization computation, not an independently machine-checked rational or formal SAT proof, and depends on a correct zero-gap solver termination. A separate human or independent mathematical audit has not been carried out. A logically equivalent result in unindexed or inaccessible literature cannot be excluded absolutely.

## References
1. C. J. Mitchell, *Searching for binary orientable sequences*, arXiv:2610.33601v1, first public 2026-10-24. https://arxiv.org/abs/2610.33601
2. C. J. Mitchell and P. R. Wild, *New orientable sequences*, arXiv:2507.02526v1, first public 2025-07-03; *Acta Informatica* 63 (2026), article 14. https://arxiv.org/abs/2507.02526 ; https://doi.org/10.1007/s00236-026-00528-z
3. D. Gabrić and J. Sawada, *Constructing k-ary Orientable Sequences with Asymptotically Optimal Length*, arXiv:2407.07029v1, first public 2024-07-09. https://arxiv.org/abs/2407.07029
4. *Orientable Sequences*, De Bruijn Sequences and Universal Cycles, public construction and acyclic overview. https://debruijnsequence.org/db/orientable
