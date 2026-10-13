# Vandermonde witnesses make finite-dimensional dividing bounds linearly sharp

## Finding
Work in the symmetric theory \(T_\infty\) of an infinite-dimensional vector space over an algebraically closed field equipped with a nondegenerate generic symmetric bilinear form. For every integers \(k\ge2\) and \(r\ge1\), one can construct a formula \(\varphi(x;b)\) whose parameter tuple has exactly \(r\) vector-sort entries and an indiscernible witnessing sequence such that:

- the family of instances is \(k\)-inconsistent but every \(k-1\) of them are consistent;
- no witnessing sequence for the same formula/type can be contained in a finite-dimensional model \(T_m\) with \(m<r(k-1)\); and
- the displayed witness is contained in a model \(T_{r(k-1)}\).

Thus the exact minimum finite vector-space dimension for this family is
\[
r(k-1).
\]
Dobrowolski and Hoffmann prove a general upper bound \(2k|V(b)|\) for finite-dimensional witnesses to \(k\)-dividing in \(T_\infty\). The construction here shows that linear dependence on both \(k\) and \(|V(b)|\) is unavoidable. In particular, any universal asymptotic bound \(Ck|V(b)|+o(k|V(b)|)\) must satisfy \(C\ge1\). This does **not** claim that their factor \(2\) is optimal.

## Assumptions and scope
The statement is for the symmetric generic-bilinear theory. Fix \(r\) mutually independent blocks
\[
E_j=\operatorname{span}(e_{j,0},\ldots,e_{j,k-2})
\qquad (1\le j\le r),
\]
with direct sum \(E=E_1\oplus\cdots\oplus E_r\), chosen inside a nondegenerate finite-dimensional subspace. Put the vectors \(e_{j,\ell}\) into the base parameter set \(A\). Let \((t_i)_{i<\omega}\) be an \(A\)-indiscernible sequence of pairwise distinct field generics and define
\[
v_j(t)=\sum_{\ell=0}^{k-2} t^{\ell}e_{j,\ell}.
\]
Use the parameter tuple
\[
b(t)=(v_1(t),\ldots,v_r(t),t)
\]
and the formula, in vector variables \(x_1,\ldots,x_r\),
\[
\varphi(x;b(t)):=\bigwedge_{j=1}^{r}[x_j,v_j(t)]=t^{k-1}.
\]
Here \([\cdot,\cdot]\) denotes the bilinear form. The count \(|V(b)|=r\) counts only vector-sort coordinates of the parameter tuple, matching the convention in the published bound.

## Proof
Take distinct scalars \(s_1,\ldots,s_q\) from the witnessing sequence, with \(q\le k-1\). For a fixed block \(j\), the vectors \(v_j(s_a)\) are linearly independent because their coefficient matrix in the basis \(e_{j,0},\ldots,e_{j,k-2}\) is a \(q\times(k-1)\) Vandermonde matrix of rank \(q\). Nondegeneracy of the bilinear form implies that the linear functionals \(x\mapsto[x,v_j(s_a)]\) are independent, so one can choose \(x_j\) satisfying
\[
[x_j,v_j(s_a)]=s_a^{k-1}\qquad(1\le a\le q).
\]
The blocks can be solved independently. Hence any \(k-1\) instances of \(\varphi\) are consistent.

Now take \(k\) distinct scalars \(s_1,\ldots,s_k\). For any fixed \(x_j\),
\[
[x_j,v_j(t)]=\sum_{\ell=0}^{k-2}[x_j,e_{j,\ell}]t^{\ell}
\]
is a polynomial of degree at most \(k-2\). It cannot agree with \(t^{k-1}\) at \(k\) distinct field elements: their difference is a nonzero polynomial of degree \(k-1\) with at most \(k-1\) roots. Therefore any \(k\) instances are inconsistent, and \(\varphi\) \(k\)-divides over \(A\).

For the lower bound on witness dimension, consider any \(A\)-indiscernible sequence witnessing \(k\)-dividing for this same parameter type. The scalar coordinates are either all equal or pairwise distinct, since equality has a constant truth value on increasing pairs of an indiscernible sequence. They cannot all be equal: then the parameters, and hence the consistent formula instance, would repeat and could not be \(k\)-inconsistent. Thus they are pairwise distinct. The first \(k-1\) vectors in each block are Vandermonde-independent. Because the \(r\) blocks form a direct sum, those parameter vectors span a space of dimension exactly
\[
r(k-1).
\]
Every finite-dimensional submodel containing the witnessing sequence therefore has vector dimension at least \(r(k-1)\).

Conversely, every vector parameter in the constructed sequence lies in the fixed nondegenerate space \(E\) of dimension \(r(k-1)\). Enlarging the scalar field sort to an algebraically closed field containing all \(t_i\) gives a model \(T_{r(k-1)}\) containing the complete witnessing sequence. The minimum is therefore exact.

Dobrowolski--Hoffmann's general theorem gives a witness in dimension \(2k|V(b)|=2kr\). Comparing this with the exact family \(r(k-1)\) proves linear-order sharpness and the asymptotic leading-constant lower bound \(C\ge1\).

## Verification
The bundled `verify.py` performs an exact rational-rank check of the finite linear-algebra core for \(2\le k\le10\) and \(1\le r\le5\). For each \(k\), it verifies that every Vandermonde system with fewer than \(k\) sample points has equal coefficient and augmented rank, while the \(k\)-point system has coefficient rank \(k-1\) and augmented rank \(k\). It also checks block additivity of the dimension lower bound and its comparison with the published \(2kr\) upper bound. The run returns `VERIFY_OK 198 exact rank assertions`.

This finite checker is supplementary: the proof for arbitrary \(k,r\) is the Vandermonde/root-count argument above.

## Relationship to prior work
Dobrowolski and Hoffmann prove that if \(\varphi(x,b)\) \(k\)-divides over a countable base in \(T_\infty\), then a witnessing indiscernible sequence can be found inside a model of vector dimension \(2k|V(b)|\); they use this to show dividing is finite and, consequently, that forking equals dividing in \(T_\infty\). Their paper does not state a lower-bound family or a sharpness result for the \(2k|V(b)|\) dimension estimate.

Targeted searches for the exact lower-bound form, Vandermonde witnesses, finite-dimensional sharpness, and equivalent asymptotic formulations found the published upper bound and general work on generic bilinear forms, but no matching lower-bound theorem. Searches of the existing result ledger likewise found only an unrelated finite-field bilinear-space orbit enumeration. The retained originality claim is therefore restricted to the explicit family, the exact minimum \(r(k-1)\), and the resulting linear-order sharpness statement.

## Limitations
The result does not improve the universal upper bound \(2k|V(b)|\), and it does not prove that the constant \(2\) is best possible. It gives a lower family whose asymptotic leading constant is \(1\). The construction is presented only for the symmetric theory; alternating forms introduce parity restrictions on finite nondegenerate dimensions and are not claimed here. Because the construction is elementary once the published upper bound is known, an uncatalogued folklore antecedent remains possible.

## References
1. Jan Dobrowolski and Daniel Max Hoffmann, *On rank not only in NSOP1 theories*, arXiv:2111.02389; Journal of Symbolic Logic, DOI:10.1017/jsl.2024.9. In the journal version, Proposition 4.4 contains the finite-dimensional witness bound \(2k|V(b)|\).
