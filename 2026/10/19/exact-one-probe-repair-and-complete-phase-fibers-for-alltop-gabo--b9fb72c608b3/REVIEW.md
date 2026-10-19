# Scientific review: Alltop Gabor phase fibers and one-probe repair

## Correctness — PASS

Direct Hermitian projector proof: planar differences imply q mutually unbiased flat bases; centered projectors for distinct bases are Hilbert-Schmidt orthogonal, each block rank q-1, so their span is all constant-diagonal Hermitian matrices of dimension q²-q+1. The kernel is exactly traceless diagonal. Equality of rank-one measurements forces matched offdiagonal products and trace; pairwise products classify all supports, and every nonzero diagonal rank≤2 difference is a two-site signed diagonal. Supplemental ww* kills all such differences iff its squared coordinate magnitudes are pairwise unequal. Rank adds one. Sorting squared magnitudes gives sharp spacing ≤2/[q(q−1)] with unique equality profile. Explicit independent computations verified MUBs for q=5,7,11,25; Hermitian ranks for q=5,7,11; and representative fibers, criterion and contrast. Finite tests are corroboration, not general proof.

## Originality — PASS (best knowledge)

Full primary source on Alltop functions develops planar difference and MUB construction, not the exact pure-state fiber classification, sharp iff single supplemental probe, or contrast optimizer. published-finding corpus queried exact phrases and tomography/MUB aliases; closest returned projector-span classifications involve inequivalent windows, and existing own claims concern geometric Gabor windows and different defect geometry. General rank-two-kernel and MUB facts are explicitly acknowledged as standard, and bibliographic residual risk remains. Relevant sources: Price–Hall–Bartlett (DOI 10.1007/s10801-022-01187-2); Carmeli et al. (arXiv:1604.02970); Wang–Shang (arXiv:1711.07585, abstract only). The strongest plausible unresolved equivalent is a formulation using a missing mutually unbiased computational basis and a rank-two diagonal Hermitian kernel. Absence from indexed searches is not a guarantee of novelty.

## Mathematical value — PASS

Determines all nonlinear ambiguity fibers for a natural infinite family of q mutually unbiased Gabor measurement bases, supplies the exact least count (one) and necessary-and-sufficient design criterion restoring universal phase retrieval even at sparse coordinate impulses, and finds the sharp unit-energy worst-impulse contrast profile. The q²−q+2 vs q² lifting-rank gap explains a concrete qualitative distinction between pure-state recovery and linear matrix tomography. The result does not purport to be a sharp noisy inverse stability theorem.

## Verification and scientific limits

Exact finite calculations are summarized in `check_output.txt` and reproduced by `check_alltop_mub.py`. They are not substituted for the general proof. The primary source was read in accessible publisher full HTML; the Wang–Shang material was only abstract-level, and that limits the originality conclusion. The projected maximin criterion is restricted to coordinate-impulse contrast, not full noise robustness.

Self-review: passed. Independent audit: not yet performed.
